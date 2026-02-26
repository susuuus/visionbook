# src/nodes/critic.py

import sys
import json
import base64
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from openai import OpenAI
from src.config import OPENAI_API_KEY, PROMPTS_DIR

client = OpenAI(api_key=OPENAI_API_KEY)
SYSTEM = (PROMPTS_DIR / "critic_system.txt").read_text()

def critique(reference_img: str | Path, rendered_img: str | Path) -> dict:
    ref_b64   = base64.b64encode(Path(reference_img).read_bytes()).decode()
    rend_b64  = base64.b64encode(Path(rendered_img).read_bytes()).decode()

    resp = client.chat.completions.create(
        model="gpt-4o",
        max_tokens=2048,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": [
                {
                    "type": "text",
                    "text": "REFERENCE image (ground truth):"
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{ref_b64}"}
                },
                {
                    "type": "text",
                    "text": "RENDERED image (current animation output):"
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{rend_b64}"}
                },
                {
                    "type": "text",
                    "text": "Compare these two images and return your analysis as JSON."
                }
            ]}
        ]
    )

    raw = resp.choices[0].message.content.strip()

    # strip markdown fences if model adds them
    if raw.startswith("```"):
        lines = raw.split("\n")
        raw   = "\n".join(lines[1:])
        raw   = raw[:raw.rfind("```")]
    raw = raw.strip()

    result = json.loads(raw)

    # save critique next to rendered image
    out_path = Path(rendered_img).with_suffix(".critique.json")
    out_path.write_text(json.dumps(result, indent=2))
    print(f"[critic] Saved critique → {out_path}")
    print(f"[critic] Pass: {result.get('pass')}")

    return result

if __name__ == "__main__":
    try:
        reference = Path('/Users/su/Documents/su/visionbook/logs.agents/src/figures/example_homography.png')
        rendered  = Path('/Users/su/Documents/su/visionbook/logs.agents/outputs/media/videos/example_homography/480p15/AnimatedFigure.mp4')

        # extract a frame from the mp4 to compare as image
        import subprocess
        frame_path = rendered.with_suffix(".png")
        subprocess.run([
            "ffmpeg", "-i", str(rendered),
            "-vf", "select=eq(n\\,0)",  # extract first frame
            "-vframes", "1",
            str(frame_path), "-y"
        ], check=True)

        result = critique(reference, frame_path)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {e}")