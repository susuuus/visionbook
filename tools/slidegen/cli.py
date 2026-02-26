from __future__ import annotations

import argparse
import json
from pathlib import Path

from .chapter_parser import parse_qmd
from .render_revealjs import render_revealjs_qmd
from .slidespec import SlideSpec
from .storyboard import storyboard_from_chapter_path


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def cmd_extract(args: argparse.Namespace) -> int:
    chapter_path = Path(args.chapter)
    outline = parse_qmd(_read_text(chapter_path), fallback_title=chapter_path.stem)
    payload = {
        "title": outline.title,
        "headings": outline.headings,
        "questions": outline.questions,
        "figures": [{"path": f.path, "caption": f.caption, "id": f.id} for f in outline.figures],
        "equations": outline.equations,
    }
    text = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


def cmd_storyboard(args: argparse.Namespace) -> int:
    spec = storyboard_from_chapter_path(
        args.chapter,
        subtitle=args.subtitle,
        hook_questions=not args.no_hook_questions,
        max_hook_questions=int(args.max_hook_questions),
    )
    out_path = Path(args.out)
    out_path.write_text(json.dumps(spec.to_json_dict(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


def cmd_render(args: argparse.Namespace) -> int:
    spec_path = Path(args.slidespec)
    data = json.loads(_read_text(spec_path))
    spec = SlideSpec.from_json_dict(data)
    qmd = render_revealjs_qmd(spec)
    Path(args.out).write_text(qmd, encoding="utf-8")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="slidegen")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_extract = sub.add_parser("extract", help="Extract outline (headings, figures, questions)")
    p_extract.add_argument("chapter", help="Path to chapter .qmd")
    p_extract.add_argument("--out", help="Write JSON to this path")
    p_extract.set_defaults(func=cmd_extract)

    p_story = sub.add_parser("storyboard", help="Create a baseline SlideSpec JSON from chapter")
    p_story.add_argument("chapter", help="Path to chapter .qmd")
    p_story.add_argument("--subtitle", default=None)
    p_story.add_argument(
        "--no-hook-questions",
        action="store_true",
        help="Disable hook question slides (default: enabled if questions exist)",
    )
    p_story.add_argument(
        "--max-hook-questions",
        default=1,
        help="Maximum number of hook questions to include (default: 1)",
    )
    p_story.add_argument("--out", required=True, help="Where to write SlideSpec JSON")
    p_story.set_defaults(func=cmd_storyboard)

    p_render = sub.add_parser("render", help="Render RevealJS .qmd from SlideSpec JSON")
    p_render.add_argument("slidespec", help="Path to SlideSpec JSON")
    p_render.add_argument("--out", required=True, help="Where to write output .qmd")
    p_render.set_defaults(func=cmd_render)

    return p


def main() -> int:
    p = build_parser()
    args = p.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
