"""End-to-end match loop: plan -> render -> critique -> update plan.

This implements a safe version of the "critic edits pipeline" idea:
- The critic does NOT directly rewrite detector/planner/animator code.
- Instead it emits parameter edits (actions) that we apply to plan.json.

Usage example:
  /path/to/python logs.agents/src/run_match_loop.py \
    --detector logs.agents/figures/homography/fig001/detector.json \
    --ref media/videos/ransac_manim_complete/480p15/RANSACVisualization.mp4 \
    --out logs.agents/runs/match_loop_fig001 \
    --iters 5 --quality m

Outputs:
- out/iter_XX/plan.json
- out/iter_XX/scene_from_plan.py
- out/iter_XX/media/.../*.mp4
- out/iter_XX/critic/critic_report.json + actions.json + frames/
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

import importlib.util
import sys


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


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Match loop: tune plan recipe to match a reference mp4")
    p.add_argument("--detector", required=True, help="Path to detector.json")
    p.add_argument("--ref", required=True, help="Path to reference mp4")
    p.add_argument("--out", required=True, help="Output directory")
    p.add_argument("--iters", type=int, default=5, help="Iterations")
    p.add_argument("--quality", default="m", help="Manim quality l/m/h/k")
    p.add_argument("--open", dest="open_after", action="store_true", help="Open best mp4 at the end")
    return p.parse_args()


def main() -> None:
    args = _parse_args()
    root = Path(args.out).resolve()
    root.mkdir(parents=True, exist_ok=True)

    planner = _load_module(Path("logs.agents/src/nodes/planner.py").resolve(), "planner_node")
    animator = _load_module(Path("logs.agents/src/nodes/animator.py").resolve(), "animator_node")
    critic = _load_module(Path("logs.agents/src/nodes/critic.py").resolve(), "critic_node")

    detector_path = Path(args.detector).resolve()
    detector_state = json.loads(detector_path.read_text())
    image_path = detector_path.with_name("input.png")
    plan = planner.plan_animation(
        detector_state,
        context="",
        scene_class_name="RansacFromDetector",
        image_path=str(image_path) if image_path.exists() else None,
    )

    best = {"f1": -1.0, "iter": -1, "mp4": None}

    for i in range(max(1, int(args.iters))):
        it_dir = root / f"iter_{i:02d}"
        it_dir.mkdir(parents=True, exist_ok=True)

        plan_path = it_dir / "plan.json"
        plan_path.write_text(json.dumps(plan, indent=2, allow_nan=False))

        script_path = animator.generate_manim_scene_from_plan_json(
            str(plan_path),
            str(Path(args.detector).resolve()),
            str(it_dir),
            animator.PlanDrivenAnimatorConfig(script_name="scene_from_plan.py"),
        )

        mp4 = animator._render_with_manim(script_path, "RansacFromDetector", media_dir=str(it_dir / "media"), quality=args.quality)
        if mp4 is None:
            mp4 = ""

        crit_dir = it_dir / "critic"
        detector_path = Path(args.detector).resolve()
        orig_img = detector_path.with_name("input.png")
        report = critic.critique_videos(
            args.ref,
            mp4,
            str(crit_dir),
            plan=plan,
            original_image_path=str(orig_img) if orig_img.exists() else None,
        )
        actions = critic.suggest_actions(report, plan)
        (crit_dir / "actions.json").write_text(json.dumps({"actions": actions}, indent=2, allow_nan=False))

        f1 = float((report.get("summary", {}) or {}).get("mean_edge_f1", 0.0) or 0.0)
        if f1 > best["f1"]:
            best = {"f1": f1, "iter": i, "mp4": mp4}

        if not actions:
            break
        plan = _apply_actions(plan, actions)

    (root / "best.json").write_text(json.dumps(best, indent=2, allow_nan=False))
    print(json.dumps(best, indent=2))

    if args.open_after and best.get("mp4"):
        animator._open_file(str(best["mp4"]))


if __name__ == "__main__":
    main()
