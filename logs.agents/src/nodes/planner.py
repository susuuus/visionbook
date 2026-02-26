"""Planner node (placeholder).

Original implementation removed. Restore desired implementation as needed.
"""

# Placeholder to keep module importable; replace with real code.
__all__ = []


def placeholder():
    """No-op placeholder for planner node."""
    return None

    def _pick(d: Dict[str, Any], keys: List[str]) -> Dict[str, Any]:
        return {k: d.get(k) for k in keys if k in d}

    compact_lines = [_pick(l, ["p1", "p2", "length", "angle_deg", "slope", "is_vertical"]) for l in _trim(lines, max_lines)]
    compact_circles = [_pick(c, ["center", "radius", "color"]) for c in _trim(circles, max_circles)]
    compact_points = [_pick(p, ["centroid", "color", "label"]) for p in _trim(points, max_points)]
    compact_arrows = [_pick(a, ["tail", "head", "label"]) for a in _trim(arrows, 50)]
    compact_axes = [_pick(a, ["origin", "x_axis", "y_axis"]) for a in _trim(axes, 20)]

    return {
        "image": {"width": img.get("width"), "height": img.get("height")},
        "summary": _summarize_primitives(detector_state),
        "primitives": {
            "lines": compact_lines,
            "circles": compact_circles,
            "points": compact_points,
            "arrows": compact_arrows,
            "axes": compact_axes,
            "grid": grid,
        },
    }


def _extract_json(text: str) -> Dict[str, Any]:
    """Parse JSON even if it is wrapped in fences or extra text."""
    try:
        return json.loads(text)
    except Exception:
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1 and end > start:
            return json.loads(text[start : end + 1])
        raise


def _load_settings() -> Any:
    cfg_path = Path(__file__).resolve().parents[1] / "config.py"
    spec = importlib.util.spec_from_file_location("agent_config", cfg_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load config: {cfg_path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, "Settings")()


def _load_prompt() -> str:
    prompt_path = Path(__file__).resolve().parents[2] / "prompts" / "planner.md"
    return prompt_path.read_text()


def _encode_image(path: str) -> Dict[str, Any]:
    mime, _ = mimetypes.guess_type(path)
    if not mime:
        mime = "image/png"
    data = Path(path).read_bytes()
    b64 = base64.b64encode(data).decode("utf-8")
    return {"type": "input_image", "image_url": f"data:{mime};base64,{b64}"}


def _call_llm(model: str, system_prompt: str, user_text: str, image_paths: Optional[List[str]] = None) -> str:
    try:
        from openai import OpenAI
    except Exception as exc:  # pragma: no cover - dependency dependent
        raise RuntimeError("openai package is required for LLM planner. Install it in the active env.") from exc

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not set. Set it to use the LLM planner.")

    client = OpenAI()
    content = [{"type": "input_text", "text": user_text}]
    for p in (image_paths or []):
        if p and Path(p).exists():
            content.append(_encode_image(p))

    resp = client.responses.create(
        model=model,
        input=[
            {"role": "system", "content": [{"type": "input_text", "text": system_prompt}]},
            {"role": "user", "content": content},
        ],
    )
    text = getattr(resp, "output_text", None)
    if not text:
        # Fallback for older SDKs
        text = "".join([c.text for c in resp.output[0].content if hasattr(c, "text")])
    return text


def _validate_plan(plan: Dict[str, Any]) -> Dict[str, Any]:
    """Light validation / normalization."""
    scenes = plan.get("scenes")
    if not isinstance(scenes, list) or len(scenes) == 0:
        raise ValueError("Plan missing scenes list.")
    for s in scenes:
        s.setdefault("intent", "step")
        s.setdefault("actions", ["highlight"])
        s.setdefault("objects_involved", ["all"])
        s.setdefault("narration", "")
        s.setdefault("checks", [])
    return plan


def plan_animation(
    detector_state: Dict[str, Any],
    context: str = "",
    scene_class_name: str = "RansacFromDetector",
    image_path: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a storyboard plan + a Manim recipe from detector output using an LLM."""
    summary = _summarize_primitives(detector_state)
    # For grid-only figures, skip LLM and use the detector-only template directly.
    if (
        summary.get("has_grid")
        and summary.get("num_circles", 0) == 0
        and summary.get("num_points", 0) == 0
        and summary.get("num_arrows", 0) == 0
        and summary.get("num_lines", 0) >= 12
    ):
        plan = {
            "planner": "heuristic",
            "summary": summary,
            "manim": _default_manim_recipe(detector_state, scene_class_name=scene_class_name),
            "scenes": _default_scenes(summary, context),
        }
        return _validate_plan(plan)

    settings = _load_settings()
    system_prompt = _load_prompt()
    user_payload = {
        "scene_class_name": scene_class_name,
        "context": context or "",
        "detector_summary": summary,
        "detector_compact": _compact_detector(detector_state),
    }
    raw = _call_llm(settings.planner_model, system_prompt, json.dumps(user_payload), image_paths=[image_path] if image_path else None)
    plan = _extract_json(raw)
    plan.setdefault("planner", "llm")
    # If multiple subplot-like scenes exist, prefer subplot grid template.
    try:
        scenes = plan.get("scenes") or []
        subplot_mentions = sum(
            ("subplot" in str(s.get("intent", "")).lower())
            or any("subplot" in str(obj).lower() for obj in (s.get("objects_involved") or []))
            for s in scenes
        )
        if subplot_mentions >= 2:
            manim = plan.setdefault("manim", {})
            manim.setdefault("template", "subplot_grid")
            manim.setdefault("subplot_grid", {"rows": 2, "cols": 3})
    except Exception:
        pass
    if "manim" not in plan:
        plan["manim"] = _default_manim_recipe(detector_state, scene_class_name=scene_class_name)
    if "summary" not in plan:
        plan["summary"] = _summarize_primitives(detector_state)
    return _validate_plan(plan)


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate plan.json from detector.json")
    p.add_argument("detector_json", help="Path to detector.json")
    p.add_argument("out_path", help="Path to write plan.json")
    p.add_argument("--scene", default="RansacFromDetector", help="Manim Scene class name")
    p.add_argument("--context", default="", help="Optional narration/context")
    p.add_argument("--image", default=None, help="Optional image path for VLM planning")
    return p.parse_args()


def main() -> None:
    args = _parse_args()
    detector_state = json.loads(Path(args.detector_json).read_text())
    plan = plan_animation(detector_state, context=args.context, scene_class_name=args.scene, image_path=args.image)
    Path(args.out_path).write_text(json.dumps(plan, indent=2, allow_nan=False))
    print(str(Path(args.out_path).resolve()))


if __name__ == "__main__":
    main()
