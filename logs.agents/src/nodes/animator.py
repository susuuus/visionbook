
                label_group.add(label)

        # Animate in layers for clarity.
        if len(line_group) > 0:
            self.play(LaggedStart(*[Create(m) for m in line_group], lag_ratio=0.02, run_time=2.5))
        if len(circle_group) > 0:
            self.play(LaggedStart(*[Create(m) for m in circle_group], lag_ratio=0.03, run_time=1.5))
        if len(label_group) > 0:
            self.play(LaggedStart(*[FadeIn(m) for m in label_group], lag_ratio=0.04, run_time=1.2))
        self.wait(1.0)
'''


def _render_subplot_grid_script(manim_recipe: Dict[str, Any], detector_json_name: str = "detector.json") -> str:
    """Render primitives grouped into a grid of subplots and animate per subplot."""
    scene_class_name = str(manim_recipe.get("scene_class_name") or "FigureSubplots")
    bg = _color_literal(str(manim_recipe.get("background_color") or "WHITE"))
    pad = float(manim_recipe.get("frame_padding") or 0.90)
    grid_cfg = manim_recipe.get("subplot_grid") or {}
    rows = int(grid_cfg.get("rows", 2) or 2)
    cols = int(grid_cfg.get("cols", 3) or 3)

    line_cfg = manim_recipe.get("line") or {}
    circle_cfg = manim_recipe.get("circle") or {}
    labels_cfg = manim_recipe.get("labels") or {}

    min_len = float(line_cfg.get("min_length_px") or 80.0)
    line_sw = float(line_cfg.get("stroke_width") or 3.0)
    long_len = float(line_cfg.get("long_length_px") or (min_len * 3.5))
    long_col = _color_literal(str(line_cfg.get("long_color") or "BLACK"))
    short_col = _color_literal(str(line_cfg.get("short_color") or "RED"))

    circle_sw = float(circle_cfg.get("stroke_width") or 2.2)
    fill_colored = float(circle_cfg.get("fill_opacity_colored") or 1.0)
    fill_other = float(circle_cfg.get("fill_opacity_other") or 0.0)

    labels_enabled = bool(labels_cfg.get("enabled", True))
    min_font = int(labels_cfg.get("min_font_size") or 10)
    font_scale = float(labels_cfg.get("font_size_scale") or 1.5)
    label_color = _color_literal(str(labels_cfg.get("color") or "BLACK"))

    return f'''from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Tuple

from manim import (
    Scene,
    config,
    Line,
    Circle,
    Text,
    VGroup,
    Create,
    FadeIn,
    LaggedStart,
    RED,
    BLUE,
    TEAL,
    GRAY,
    LIGHT_GRAY,
    BLACK,
    WHITE,
)

GREY = GRAY
DIM_GRAY = GRAY


DATA_PATH = Path(__file__).with_name("{detector_json_name}")


def _to_manim_point(x: float, y: float, w: float, h: float, scale: float) -> Tuple[float, float, float]:
    mx = (x - (w / 2.0)) * scale
    my = ((h / 2.0) - y) * scale
    return (mx, my, 0.0)


def _color_for_circle(color: str):
    c = (color or "").lower()
    if c == "red":
        return RED
    if c == "cyan":
        return TEAL
    if c == "gray":
        return GRAY
    if c == "black":
        return BLACK
    return WHITE


def _cell_index(x: float, y: float, w: float, h: float, rows: int, cols: int) -> int:
    cw = w / float(cols)
    ch = h / float(rows)
    c = int(min(cols - 1, max(0, x // cw)))
    r = int(min(rows - 1, max(0, y // ch)))
    return r * cols + c


class {scene_class_name}(Scene):
    def construct(self):
        config.background_color = {bg}
        self.camera.background_color = {bg}
        data: Dict[str, Any] = json.loads(DATA_PATH.read_text())
        w = float(data["image"]["width"])
        h = float(data["image"]["height"])

        scale = min(config.frame_width / w, config.frame_height / h) * {pad}

        lines = data.get("primitives", {{}}).get("lines", [])
        circles = data.get("primitives", {{}}).get("circles", [])
        labels = data.get("primitives", {{}}).get("text_labels", [])

        groups = [VGroup() for _ in range({rows} * {cols})]

        for ln in lines:
            length = float(ln.get("length", 0.0))
            if length < {min_len}:
                continue
            p1 = ln["p1"]
            p2 = ln["p2"]
            mx = (p1[0] + p2[0]) * 0.5
            my = (p1[1] + p2[1]) * 0.5
            idx = _cell_index(mx, my, w, h, {rows}, {cols})
            color = {long_col} if length >= {long_len} else {short_col}
            groups[idx].add(
                Line(
                    _to_manim_point(p1[0], p1[1], w, h, scale),
                    _to_manim_point(p2[0], p2[1], w, h, scale),
                    color=color,
                    stroke_width={line_sw},
                )
            )

        for c in circles:
            center = c["center"]
            radius = float(c.get("radius", 6))
            idx = _cell_index(center[0], center[1], w, h, {rows}, {cols})
            color = _color_for_circle(c.get("color", ""))
            fill_opacity = {fill_colored} if c.get("color") in {{"red", "cyan"}} else {fill_other}
            circle = Circle(radius=radius * scale, color=color, stroke_width={circle_sw}, fill_color=color, fill_opacity=fill_opacity)
            circle.move_to(_to_manim_point(center[0], center[1], w, h, scale))
            groups[idx].add(circle)

        if {labels_enabled}:
            for t in labels:
                text = str(t.get("text", "")).strip()
                if not text:
                    continue
                cx, cy = t.get("centroid", [0, 0])
                idx = _cell_index(cx, cy, w, h, {rows}, {cols})
                font_size_px = float(t.get("font_size_estimate", 12))
                font_size = max({min_font}, font_size_px * scale * {font_scale})
                label = Text(text, font_size=font_size, color={label_color})
                label.move_to(_to_manim_point(cx, cy, w, h, scale))
                groups[idx].add(label)

        # Animate each subplot group in sequence.
        for i, g in enumerate(groups):
            if len(g) == 0:
                continue
            self.play(LaggedStart(*[FadeIn(m) for m in g], lag_ratio=0.02, run_time=1.2))
            self.wait(0.4)

        self.wait(1.0)
'''


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate a Manim scene script from detector.json")
    p.add_argument("detector_json", help="Path to detector.json")
    p.add_argument("out_dir", help="Output directory for scene script")
    p.add_argument("--plan", default=None, help="Optional path to plan.json (enables ransac-style template)")
    p.add_argument("--scene", default=None, help="Scene class name (optional)")
    p.add_argument("--render", action="store_true", help="Run manim to render an mp4")
    p.add_argument("--quality", default="m", help="Render quality: l/m/h/k (default: m)")
    p.add_argument("--open", dest="open_after", action="store_true", help="Open the rendered mp4 after rendering")
    return p.parse_args()


def main() -> None:
    args = _parse_args()
    out_dir = str(Path(args.out_dir).resolve())
    media_dir = str(Path(out_dir) / "media")

    if args.plan:
        plan_cfg = PlanDrivenAnimatorConfig(script_name="scene_from_plan.py")
        script = generate_manim_scene_from_plan_json(args.plan, args.detector_json, out_dir, plan_cfg)
        scene = "RansacFromDetector"
        try:
            recipe = (json.loads(Path(args.plan).read_text()).get("manim") or {})
            scene = str(recipe.get("scene_class_name") or scene)
        except Exception:
            pass
    else:
        scene = str(args.scene or ManimAnimatorConfig.scene_class_name)
        cfg = ManimAnimatorConfig(scene_class_name=scene)
        script = generate_manim_scene_from_detector_json(args.detector_json, out_dir, cfg)

    print(script)

    if args.render:
        mp4 = _render_with_manim(script, scene, media_dir=media_dir, quality=args.quality)
        if mp4:
            print(mp4)
            if args.open_after:
                _open_file(mp4)


if __name__ == "__main__":
    main()
