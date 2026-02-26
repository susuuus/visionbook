from __future__ import annotations

from .slidespec import SlideSpec, validate_slidespec


def _yaml_bool(x: bool) -> str:
    return "true" if x else "false"


def render_revealjs_qmd(spec: SlideSpec) -> str:
    errors = validate_slidespec(spec)
    if errors:
        raise ValueError("Invalid SlideSpec:\n- " + "\n- ".join(errors))

    r = spec.revealjs

    header_lines: list[str] = [
        "---",
        f"title: {spec.title}",
    ]
    if spec.subtitle:
        header_lines.append(f"subtitle: {spec.subtitle}")
    if spec.author:
        header_lines.append(f"author: {spec.author}")

    header_lines += [
        "format:",
        "  revealjs:",
        f"    width: {r.width}",
        f"    height: {r.height}",
        f"    center: {_yaml_bool(r.center)}",
        f"    navigationMode: {r.navigationMode}",
        f"    controlsLayout: {r.controlsLayout}",
        f"    controlsTutorial: {_yaml_bool(r.controlsTutorial)}",
        f"    hash: {_yaml_bool(r.hash)}",
        f"    history: {_yaml_bool(r.history)}",
        f"    transition: {r.transition}",
        f"    backgroundTransition: {r.backgroundTransition}",
        f"    slideNumber: {_yaml_bool(r.slideNumber)}",
        f"    chalkboard: {_yaml_bool(r.chalkboard)}",
        f"    previewLinks: {_yaml_bool(r.previewLinks)}",
        f"    reference-location: {r.reference_location}",
        "bibliography:",
        "  - all.bib",
        "  - visionbib.bib",
        "---",
        "",
    ]

    body: list[str] = []

    # Learning objectives slide (optional)
    if spec.learning_objectives:
        body += ["## Today’s goals", "", "::: {.incremental}", ""]
        for obj in spec.learning_objectives:
            body.append(f"- {obj}")
        body += ["", ":::", ""]

    for slide in spec.slides:
        body.append(f"## {slide.title}")
        body.append("")

        # Builds: if present, we render them as incremental fragments.
        # Otherwise, use a simple bullet list.
        if slide.builds:
            body.append("::: {.incremental}")
            body.append("")
            for b in slide.builds:
                if b.kind == "bullets":
                    for item in b.content:
                        body.append(f"- {item}")
                elif b.kind == "text":
                    body.append(str(b.content))
                elif b.kind == "equation":
                    body.append("$$")
                    body.append(str(b.content))
                    body.append("$$")
                elif b.kind == "figure":
                    body.append(f"![]({b.content})")
            body.append("")
            body.append(":::")
            body.append("")
        elif slide.bullets:
            body.append("::: {.incremental}")
            body.append("")
            for item in slide.bullets:
                body.append(f"- {item}")
            body.append("")
            body.append(":::")
            body.append("")

        if slide.equation and not slide.builds:
            body.append("$$")
            body.append(slide.equation)
            body.append("$$")
            body.append("")

        if slide.figure:
            # Keep figure centered and reasonably large.
            cap = f"\n\n{slide.figure_caption}" if slide.figure_caption else ""
            body.append(f"![]({slide.figure}){{width=80%}}{cap}")
            body.append("")

        if slide.speaker_notes or slide.timing_sec:
            body.append("::: notes")
            if slide.timing_sec:
                body.append(f"Time budget: ~{slide.timing_sec}s")
                body.append("")
            if slide.speaker_notes:
                body.append(slide.speaker_notes)
            body.append(":::")
            body.append("")

    return "\n".join(header_lines + body).rstrip() + "\n"
