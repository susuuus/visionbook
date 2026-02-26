from __future__ import annotations

from .chapter_parser import ChapterOutline, parse_qmd
from .slidespec import BuildStep, Slide, SlideSpec


def _pick_hook_questions(outline: ChapterOutline, *, max_q: int = 1) -> list[str]:
    """Pick up to max_q hook questions from the chapter.

    The parser already ranks questions; here we just de-duplicate near-substrings.
    """

    picked: list[str] = []
    for q in outline.questions:
        q_norm = " ".join(q.lower().split())
        if any(
            q_norm in " ".join(p.lower().split())
            or " ".join(p.lower().split()) in q_norm
            for p in picked
        ):
            continue
        picked.append(q)
        if len(picked) >= max_q:
            break
    return picked


def _pick_key_figures(outline: ChapterOutline) -> list[tuple[str, str]]:
    # Generic heuristic: keep the first few figures, de-duped by path.
    seen: set[str] = set()
    out: list[tuple[str, str]] = []
    for f in outline.figures:
        if f.path in seen:
            continue
        seen.add(f.path)
        out.append((f.path, f.caption))
        if len(out) >= 8:
            break
    return out


def _derive_learning_objectives(outline: ChapterOutline, *, max_obj: int = 4) -> list[str]:
    # Minimal, generic objectives based on headings (works across chapters).
    headings = [h.strip() for h in outline.headings if h.strip()]
    # drop the chapter title if present as the first heading
    if headings and headings[0].lower() == outline.title.lower():
        headings = headings[1:]

    objs: list[str] = []
    for h in headings:
        # Keep it short; headings can be long.
        short = h
        if len(short) > 90:
            short = short[:87].rstrip() + "…"
        objs.append(f"Understand: {short}")
        if len(objs) >= max_obj:
            break
    return objs


def storyboard_from_chapter_text(
    chapter_text: str,
    *,
    source_path: str | None = None,
    subtitle: str | None = None,
    author: str | None = "Foundations of Computer Vision",
    hook_questions: bool = True,
    max_hook_questions: int = 1,
) -> SlideSpec:
    outline = parse_qmd(chapter_text)

    learning_objectives = _derive_learning_objectives(outline)

    slides: list[Slide] = []

    # Title
    slides.append(
        Slide(
            title=outline.title,
            type="title",
            bullets=[],
            speaker_notes="High-level framing: CNNs vs global communication; what we’ll learn today.",
            timing_sec=30,
        )
    )

    # Hook questions (optional)
    if hook_questions and max_hook_questions > 0:
        for q in _pick_hook_questions(outline, max_q=max_hook_questions):
            slides.append(
                Slide(
                    title="The Question",
                    type="hook_question",
                    bullets=[q],
                    speaker_notes="Ask for predictions; don’t answer immediately.",
                    timing_sec=30,
                    builds=[BuildStep(kind="bullets", content=[q], notes="Reveal after audience thinks")],
                )
            )

    # A few core sections as concept slides
    # We keep it minimal and lecture-like: 1–3 bullets + one figure where possible.
    key_figs = _pick_key_figures(outline)

    def fig(path_substr: str) -> tuple[str, str] | None:
        for p, c in key_figs:
            if path_substr in p:
                return (p, c)
        return None

    cnn_lim = fig("CNN_limitations")
    tokenization = fig("tokenization")
    pos_codes = fig("positional")

    slides.append(
        Slide(
            title="Why Transformers? A CNN Limitation",
            type="concept",
            bullets=[
                "CNN kernels are local; far apart patches don’t directly interact",
                "Global comparisons require deep stacks or large kernels",
                "Goal: pass messages across long distances efficiently",
            ],
            figure=cnn_lim[0] if cnn_lim else None,
            figure_caption=cnn_lim[1] if cnn_lim else None,
            speaker_notes="Use the figure to show which nodes can/can’t communicate; motivate attention.",
            timing_sec=75,
        )
    )

    slides.append(
        Slide(
            title="New idea #1: tokens",
            type="concept",
            bullets=[
                "Token = vector-valued bundle of neurons (encapsulated information)",
                "Tokenization: map each patch → a token code vector",
                "Then operate on arrays of tokens (not raw pixels)",
            ],
            figure=tokenization[0] if tokenization else None,
            figure_caption=tokenization[1] if tokenization else None,
            speaker_notes="Connect to the book’s framing: tokens are a new data type.",
            timing_sec=75,
        )
    )

    slides.append(
        Slide(
            title="New idea #2: attention",
            type="concept",
            bullets=[
                "Instead of fixed mixing weights, attention computes weights from the input",
                "This lets the model focus on the relevant tokens for the current query",
            ],
            speaker_notes="Bridge to Q/K/V: queries ask, keys match, values provide content.",
            timing_sec=60,
        )
    )

    slides.append(
        Slide(
            title="Self-attention (Q/K/V)",
            type="equation",
            bullets=[
                "Queries: what am I looking for?",
                "Keys: what do I contain / what am I?",
                "Values: what information do I pass along?",
            ],
            equation=r"\text{Attn}(Q,K,V)=\text{softmax}\left(\frac{QK^\mathsf{T}}{\sqrt{d}}\right)V",
            speaker_notes="Do a slow walkthrough: similarity → softmax → weighted sum.",
            timing_sec=90,
            builds=[
                BuildStep(kind="bullets", content=["Queries: what am I looking for?"], notes="ask an example question"),
                BuildStep(kind="bullets", content=["Keys: what do I contain / what am I?"], notes="match to query"),
                BuildStep(kind="bullets", content=["Values: what information do I pass along?"], notes="weighted sum"),
                BuildStep(kind="equation", content=r"\text{softmax}\left(\frac{QK^\mathsf{T}}{\sqrt{d}}\right)V", notes="reveal last"),
            ],
        )
    )

    slides.append(
        Slide(
            title="New idea #3: positional encoding",
            type="figure_walkthrough",
            bullets=[
                "Attention is permutation-equivariant over tokens",
                "Images are not: patch order (x,y) matters",
                "So we add a position-dependent code to each token",
            ],
            figure=pos_codes[0] if pos_codes else None,
            figure_caption=pos_codes[1] if pos_codes else None,
            speaker_notes="Explain the failure case: shuffled patches; then positional codes fix it.",
            timing_sec=75,
        )
    )

    slides.append(
        Slide(
            title="Checkpoint",
            type="checkpoint",
            bullets=[
                "What are the 3 innovations? (tokens, attention, positional encoding)",
                "What problem did each innovation solve?",
            ],
            speaker_notes="Pause and ask for a recap; call on 1–2 students.",
            timing_sec=45,
            builds=[BuildStep(kind="bullets", content=["What are the 3 innovations? (tokens, attention, positional encoding)"], notes=None)],
        )
    )

    slides.append(
        Slide(
            title="Summary",
            type="summary",
            bullets=[
                "Transformers enable global communication early",
                "Attention = data-dependent mixing over tokens",
                "Positional encoding injects spatial order",
            ],
            speaker_notes="Close with when/why to use ViTs and what breaks (quadratic tokens).",
            timing_sec=45,
        )
    )

    spec = SlideSpec(
        title=outline.title,
        subtitle=subtitle,
        author=author,
        source_chapter=source_path,
        learning_objectives=learning_objectives,
        slides=slides,
    )

    return spec


def storyboard_from_chapter_path(
    path: str,
    *,
    subtitle: str | None = None,
    hook_questions: bool = True,
    max_hook_questions: int = 1,
) -> SlideSpec:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return storyboard_from_chapter_text(
        text,
        source_path=path,
        subtitle=subtitle,
        hook_questions=hook_questions,
        max_hook_questions=max_hook_questions,
    )
