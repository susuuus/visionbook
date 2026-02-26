# src/nodes/animator.py

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from openai import OpenAI
from src.config import OPENAI_API_KEY, ANIMATOR_MODEL, PROMPTS_DIR

client = OpenAI(api_key=OPENAI_API_KEY)
SYSTEM = (PROMPTS_DIR / "animator_system.txt").read_text()

def generate(description: str | Path, img_path: str | Path = None, correction: str = None, save: bool = True) -> str:
    # if a path is passed, read the description from the file
    if isinstance(description, (str, Path)):
        p = Path(description)
        if p.suffix == ".txt" and p.exists():
            if img_path is None:
                img_path = p
            description = p.read_text()

    user_msg = (
        "IMPORTANT: Return ONLY valid Python Manim code. "
        "Do NOT return React, JavaScript, or any other language. "
        "Do NOT use markdown fences. "
        "The code must define a class named AnimatedFigure(Scene).\n\n"
        f"Figure description:\n{description}"
    )

    if correction:
        user_msg += f"\n\nCorrections from previous iteration — apply ALL of these:\n{correction}"

    resp = client.chat.completions.create(
        model=ANIMATOR_MODEL,
        max_tokens=8192,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user",   "content": user_msg}
        ]
    )
    code = resp.choices[0].message.content.strip()

    # strip markdown fences if model adds them
    if code.startswith("```"):
        lines = code.split("\n")
        code  = "\n".join(lines[1:])
        code  = code[:code.rfind("```")]
    code = code.strip()

    # validate generated code
    if "from manim import" not in code and "import manim" not in code:
        raise ValueError("[animator] Model did not return Manim code.")
    if "self.add(" in code and "self.play(" not in code:
        raise ValueError("[animator] Code uses self.add() with no self.play() — scene is static.")
    if "apply_matrix" in code:
        raise ValueError("[animator] Code uses apply_matrix() instead of DLT homography.")

    if save and img_path is not None:
        out_dir = Path(img_path).parent.parent / "outputs"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / Path(str(img_path).replace(".description", "")).with_suffix(".py").name
        out_path.write_text(code)
        print(f"[animator] Saved code → {out_path}")

    return code

if __name__ == "__main__":
    try:
        desc_path = Path('/Users/su/Documents/su/visionbook/logs.agents/src/figures/example_homography.description.txt')
        result = generate(desc_path, img_path=desc_path)
        print(result)
    except Exception as e:
        print(f"Error: {e}")