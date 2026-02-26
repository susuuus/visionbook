"""Reusable agent loop using LangGraph: plan -> render -> critique -> act -> loop.

This wraps the existing in-repo nodes:
- logs.agents/src/nodes/planner.py
- logs.agents/src/nodes/animator.py
- logs.agents/src/nodes/critic.py

Design goals:
- Deterministic + local (no LLM required)
- Iteration artifacts written under out/iter_XX/
- Resumable: write out/state_latest.json after each iteration

Usage:
  /path/to/python logs.agents/src/run_match_loop_langgraph.py \
    --detector logs.agents/figures/homography/fig001/detector.json \
    --ref media/videos/ransac_manim_complete/480p15/RANSACVisualization.mp4 \
    --out logs.agents/runs/match_loop_fig001_langgraph \
    --iters 5 --quality l

Resume:
  ... --resume
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, TypedDict


def _load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load module: {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def _set_nested(d: Dict[str, Any], path: str, value: Any) -> None:
    parts = path.split(".")
    cur: Any = d
    for p in parts[:-1]:
        nxt = cur.get(p)
        if not isinstance(nxt, dict):
            nxt = {}
            cur[p] = nxt
        cur = nxt
    cur[parts[-1]] = value


def _get_nested(d: Dict[str, Any], path: str) -> Any:
    cur: Any = d
    for p in path.split("."):
        if not isinstance(cur, dict):
            return None
        cur = cur.get(p)
    return cur


def _apply_actions(plan: Dict[str, Any], actions: List[Dict[str, Any]]) -> Dict[str, Any]:
    plan = json.loads(json.dumps(plan))  # cheap deep copy
    for a in actions:
        op = str(a.get("op", "")).lower().strip()
        path = str(a.get("path", "")).strip()
        if not op or not path:
            continue
        if op == "set":
            _set_nested(plan, path, a.get("value"))
        elif op == "mul":
            cur = _get_nested(plan, path)
            try:
                cur_f = float(cur)
                mul = float(a.get("value"))
                _set_nested(plan, path, cur_f * mul)
            except Exception:
                continue
        elif op == "clamp":
            cur = _get_nested(plan, path)
            try:
                cur_f = float(cur)
                mn = float(a.get("min"))
                mx = float(a.get("max"))
                _set_nested(plan, path, float(max(mn, min(mx, cur_f))))
            except Exception:
                continue
    return plan


class MatchState(TypedDict, total=False):
    detector_path: str
    ref_mp4: str
    out_dir: str

    iter: int
    max_iters: int
    quality: str
    scene_class_name: str

    detector_state: Dict[str, Any]
    plan: Dict[str, Any]

    iter_dir: str
    plan_path: str
    script_path: str
    mp4_path: str

    critic_dir: str
    critic_report: Dict[str, Any]
    actions: List[Dict[str, Any]]

    best_f1: float
    best_mp4: Optional[str]
    best_iter: int


def _write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, allow_nan=False))


def _state_paths(out_dir: Path) -> Dict[str, Path]:
    return {
        "latest": out_dir / "state_latest.json",
        "best": out_dir / "best.json",
    }


def _node_prepare(state: MatchState) -> MatchState:
    out_dir = Path(state["out_dir"]).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    it = int(state.get("iter", 0) or 0)
    iter_dir = out_dir / f"iter_{it:02d}"
    iter_dir.mkdir(parents=True, exist_ok=True)

    detector_state = state.get("detector_state")
    if detector_state is None:
        detector_state = json.loads(Path(state["detector_path"]).read_text())

    updates: MatchState = {
        "iter_dir": str(iter_dir),
        "critic_dir": str(iter_dir / "critic"),
        "detector_state": detector_state,
    }
    return updates


def _node_plan(state: MatchState, planner_mod) -> MatchState:
    detector_state = state["detector_state"]
    scene = str(state.get("scene_class_name") or "RansacFromDetector")

    plan = state.get("plan")
    if not isinstance(plan, dict):
        detector_path = Path(state["detector_path"]).resolve()
        image_path = detector_path.with_name("input.png")
        plan = planner_mod.plan_animation(
            detector_state,
            context="",
            scene_class_name=scene,
            image_path=str(image_path) if image_path.exists() else None,
        )

    plan_path = Path(state["iter_dir"]) / "plan.json"
    _write_json(plan_path, plan)
    return {"plan": plan, "plan_path": str(plan_path)}


def _node_animate(state: MatchState, animator_mod) -> MatchState:
    it_dir = Path(state["iter_dir"]).resolve()

    scene_class_name = str(
        ((state.get("plan") or {}).get("manim") or {}).get("scene_class_name")
        or state.get("scene_class_name")
        or "RansacFromDetector"
    )

    script_path = animator_mod.generate_manim_scene_from_plan_json(
        str(Path(state["plan_path"]).resolve()),
        str(Path(state["detector_path"]).resolve()),
        str(it_dir),
        animator_mod.PlanDrivenAnimatorConfig(script_name="scene_from_plan.py"),
    )

    mp4 = animator_mod._render_with_manim(
        script_path,
        scene_class_name,
        media_dir=str(it_dir / "media"),
        quality=str(state.get("quality") or "m"),
    )

    return {"script_path": str(script_path), "mp4_path": str(mp4 or "")}


def _node_critic(state: MatchState, critic_mod) -> MatchState:
    crit_dir = Path(state["critic_dir"]).resolve()
    crit_dir.mkdir(parents=True, exist_ok=True)

    detector_path = Path(state["detector_path"]).resolve()
    orig_img = detector_path.with_name("input.png")
    report = critic_mod.critique_videos(
        state["ref_mp4"],
        state["mp4_path"],
        str(crit_dir),
        plan=state.get("plan"),
        original_image_path=str(orig_img) if orig_img.exists() else None,
    )
    _write_json(crit_dir / "critic_report.json", report)

    return {"critic_report": report}


def _node_act(state: MatchState, critic_mod) -> MatchState:
    plan = state["plan"]
    report = state["critic_report"]

    actions = critic_mod.suggest_actions(report, plan)
    _write_json(Path(state["critic_dir"]) / "actions.json", {"actions": actions})

    # Track best
    summ = report.get("summary", {}) or {}
    f1 = float(summ.get("mean_edge_f1", 0.0) or 0.0)
    best_f1 = float(state.get("best_f1", -1.0) or -1.0)
    best_mp4 = state.get("best_mp4")
    best_iter = int(state.get("best_iter", -1) or -1)

    if f1 > best_f1:
        best_f1 = f1
        best_mp4 = state.get("mp4_path")
        best_iter = int(state.get("iter", 0) or 0)

    updates: MatchState = {"actions": actions, "best_f1": best_f1, "best_mp4": best_mp4, "best_iter": best_iter}

    if actions:
        updates["plan"] = _apply_actions(plan, actions)

    updates["iter"] = int(state.get("iter", 0) or 0) + 1

    # Persist latest state after each iteration
    out_dir = Path(state["out_dir"]).resolve()
    paths = _state_paths(out_dir)
    _write_json(paths["latest"], {**state, **updates})
    _write_json(paths["best"], {"f1": best_f1, "iter": best_iter, "mp4": best_mp4})

    return updates


def _should_continue(state: MatchState) -> str:
    it = int(state.get("iter", 0) or 0)
    max_iters = int(state.get("max_iters", 5) or 5)
    if it >= max_iters:
        return "end"

    actions = state.get("actions") or []
    if not actions:
        return "end"

    return "continue"


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="LangGraph match loop: tune plan recipe to match a reference mp4")
    p.add_argument("--detector", required=True, help="Path to detector.json")
    p.add_argument("--ref", required=True, help="Path to reference mp4")
    p.add_argument("--out", required=True, help="Output directory")
    p.add_argument("--iters", type=int, default=5, help="Iterations")
    p.add_argument("--quality", default="m", help="Manim quality l/m/h/k")
    p.add_argument("--scene", default="RansacFromDetector", help="Manim Scene class name")
    p.add_argument("--open", dest="open_after", action="store_true", help="Open best mp4 at the end")
    p.add_argument("--resume", action="store_true", help="Resume from out/state_latest.json if present")
    return p.parse_args()


def main() -> None:
    args = _parse_args()

    # Import LangGraph lazily so the rest of the repo can run without it.
    from langgraph.graph import StateGraph

    out_dir = Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    planner_mod = _load_module(Path("logs.agents/src/nodes/planner.py").resolve(), "planner_node")
    animator_mod = _load_module(Path("logs.agents/src/nodes/animator.py").resolve(), "animator_node")
    critic_mod = _load_module(Path("logs.agents/src/nodes/critic.py").resolve(), "critic_node")

    base_state: MatchState = {
        "detector_path": str(Path(args.detector).resolve()),
        "ref_mp4": str(Path(args.ref).resolve()),
        "out_dir": str(out_dir),
        "iter": 0,
        "max_iters": int(args.iters),
        "quality": str(args.quality),
        "scene_class_name": str(args.scene),
        "best_f1": -1.0,
        "best_mp4": None,
        "best_iter": -1,
    }

    if args.resume:
        latest = _state_paths(out_dir)["latest"]
        if latest.exists():
            loaded = json.loads(latest.read_text())
            # Only trust a subset of fields when resuming.
            for k in [
                "iter",
                "plan",
                "best_f1",
                "best_mp4",
                "best_iter",
            ]:
                if k in loaded:
                    base_state[k] = loaded[k]

    g = StateGraph(MatchState)

    g.add_node("prepare", lambda s: _node_prepare(s))
    g.add_node("plan", lambda s: _node_plan(s, planner_mod))
    g.add_node("animate", lambda s: _node_animate(s, animator_mod))
    g.add_node("critic", lambda s: _node_critic(s, critic_mod))
    g.add_node("act", lambda s: _node_act(s, critic_mod))

    g.set_entry_point("prepare")
    g.add_edge("prepare", "plan")
    g.add_edge("plan", "animate")
    g.add_edge("animate", "critic")
    g.add_edge("critic", "act")

    g.add_conditional_edges(
        "act",
        _should_continue,
        {
            "continue": "prepare",
            "end": "__end__",
        },
    )

    app = g.compile()
    final = app.invoke(base_state)

    best = {"f1": final.get("best_f1"), "iter": final.get("best_iter"), "mp4": final.get("best_mp4")}
    _write_json(out_dir / "best.json", best)
    print(json.dumps(best, indent=2))

    if args.open_after and best.get("mp4"):
        animator_mod._open_file(str(best["mp4"]))


if __name__ == "__main__":
    main()
