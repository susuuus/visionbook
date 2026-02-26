```markdown
# logs.agents

Structured, reproducible agentic loop logs and sources for PNG-to-animation workflows.

## What this is
This folder contains:
- **Inputs** (PNG figures + optional context)
- **Intermediate artifacts** (scene graphs, plans, prompts/responses)
- **Outputs** (Manim/HTML source + rendered videos)
- **Critique + revision logs** (issues found and fixes applied)

The goal is to make every run **replayable** and easy to compare across iterations.

## Workflow (high level)
Each run follows the same loop:
1. **Detector** → extract primitives/labels (or use a stub/manual scene for MVP)
2. **Editor** → optional: sanitize/dedupe the scene graph (no reconstruction in minimal mode)
3. **Planner** → produce an animation plan (JSON storyboard)
4. **Animator** → generate Manim/HTML code and render a preview video
5. **Critic** → evaluate render and output structured issues
6. **Revise** → apply fixes and re-render (1–2 iterations)

### Minimal mode (Detector → Animator)
If you want the simplest path from a figure to a Manim scene:

1) Run the detector to produce `detector.json` next to `input.png`.
2) Generate a Manim scene script directly from that JSON:
	- `python logs.agents/src/nodes/animator_manim.py <path/to/detector.json> <out_dir>`
3) Render (if Manim is installed):
	- `manim -pqh <out_dir>/scene_detected.py DetectedFigureScene`

## Directory structure
```

logs.agents/
figures/                # input dataset (PNG + context) <chapter>/
<fig_id>/
input.png
context.txt

runs/                   # immutable logs per execution <date>*<chapter>*<fig_id>/
input.png
scene.json           # detector output (optional in MVP)
plan.json            # planner output
code/                # generated source
scene.py           # Manim
index.html         # (optional) HTML/Three.js
outputs/
render_v0.mp4
render_v1.mp4
frames/            # optional
critic_v0.json
critic_v1.json
notes.md             # optional manual notes
config.yaml          # snapshot of settings used

```

## Naming conventions
- **Figure IDs:** `fig###` (e.g., `fig001`)
- **Run IDs:** `<YYYY-MM-DD>_<chapter>_<fig_id>`
- Outputs are versioned as `v0`, `v1`, ... (one revision pass is usually enough for MVP demos).

## What to log (minimum)
For each run, save at least:
- `input.png`
- `plan.json`
- generated code (`scene.py` / `index.html`)
- `render_v0.mp4` (and `render_v1.mp4` if revised)
- `critic_v0.json` (and `critic_v1.json` if revised)

## How to reproduce a run
1. Locate the run folder under `runs/<run_id>/`
2. Use the saved `config.yaml` (if present)
3. Re-render from the saved source in `code/`
4. Compare outputs across versions (`render_v0` vs `render_v1`)

## Notes
- Early runs may use **manual or stubbed detector outputs** to validate the end-to-end loop.
- The primary objective is **repeatability**: every result should be traceable to input + prompts + code + render.
```
