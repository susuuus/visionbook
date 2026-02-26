# src/graph.py

from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END
from src.nodes import detector, animator, critic
from src.utils import renderer
from src.config import MAX_ITER, OUTPUTS_DIR
from pathlib import Path
import json, base64

class State(TypedDict):
    img_path:     str
    description:  str
    code:         str
    screenshot:   str
    correction:   Optional[str]
    iteration:    int
    passed:       bool

# ── Nodes ──────────────────────────────────────────

def detect_node(state: State) -> State:
    print("→ Detecting...")
    state["description"] = detector.describe(state["img_path"])
    print(state["description"][:200])
    return state

def animate_node(state: State) -> State:
    print(f"→ Animating (iteration {state['iteration'] + 1})...")
    state["code"] = animator.generate(
        state["description"],
        state.get("correction")
    )
    return state

def render_node(state: State) -> State:
    print("→ Rendering...")
    state["screenshot"] = renderer.screenshot(state["code"])
    return state

def critic_node(state: State) -> State:
    print("→ Critiquing...")
    result = critic.compare(state["img_path"], state["screenshot"])

    state["passed"]    = result["pass"]
    state["correction"] = result.get("correction_instructions")
    state["iteration"] += 1

    # save outputs
    fig  = Path(state["img_path"])
    out  = OUTPUTS_DIR / fig.parent.name / fig.stem
    out.mkdir(parents=True, exist_ok=True)

    i = state["iteration"]
    (out / f"iteration_{i}.py").write_text(state["code"])
    (out / f"critique_{i}.json").write_text(json.dumps(result, indent=2))
    Path(out / f"iteration_{i}.png").write_bytes(
        base64.b64decode(state["screenshot"])
    )

    print(f"   pass={state['passed']}")
    if not state["passed"]:
        print(f"   → {state['correction'][:120]}")

    if state["passed"]:
        (out / "final.py").write_text(state["code"])
        print(f"\n✓ Done — {out / 'final.py'}")

    return state

# ── Routing ────────────────────────────────────────

def should_continue(state: State) -> str:
    if state["passed"] or state["iteration"] >= MAX_ITER:
        return "end"
    return "animate"

# ── Build graph ────────────────────────────────────

def build_graph():
    graph = StateGraph(State)

    graph.add_node("detect",  detect_node)
    graph.add_node("animate", animate_node)
    graph.add_node("render",  render_node)
    graph.add_node("critic",  critic_node)

    graph.set_entry_point("detect")
    graph.add_edge("detect",  "animate")
    graph.add_edge("animate", "render")
    graph.add_edge("render",  "critic")
    graph.add_conditional_edges("critic", should_continue, {
        "animate": "animate",
        "end":     END
    })

    return graph.compile()

# ── Entry point ────────────────────────────────────

if __name__ == "__main__":
    import sys
    img_path = sys.argv[1] if len(sys.argv) > 1 else \
        "figures/homography/example_homography.png"

    app = build_graph()
    app.invoke({
        "img_path":    img_path,
        "description": "",
        "code":        "",
        "screenshot":  "",
        "correction":  None,
        "iteration":   0,
        "passed":      False
    })