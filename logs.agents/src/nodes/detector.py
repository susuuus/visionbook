# src/nodes/detector.py

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from openai import OpenAI
from src.config import OPENAI_API_KEY, DETECTOR_MODEL, PROMPTS_DIR
import base64

client = OpenAI(api_key=OPENAI_API_KEY)
SYSTEM = (PROMPTS_DIR / "detector_system.txt").read_text()

def describe(img_path: str, save: bool = True) -> str:
    img_b64 = base64.b64encode(Path(img_path).read_bytes()).decode()

    resp = client.chat.completions.create(
        model=DETECTOR_MODEL,
        max_tokens=1024,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{img_b64}"
                    }
                },
                {
                    "type": "text",
                    "text": "Describe this figure in detail following your instructions."
                }
            ]}
        ]
    )

    description = resp.choices[0].message.content.strip()

    if save:
        out_dir = Path(img_path).parent.parent / "outputs"
        out_dir.mkdir(exist_ok=True)
        out_path = out_dir / Path(img_path).with_suffix(".description.txt").name
        out_path.write_text(description)
        print(f"[detector] Saved description → {out_path}")

    return description

if __name__ == "__main__":
    try:
        result = describe('/Users/su/Documents/su/visionbook/logs.agents/figures/homography/example_homography.png')
        print(result)
    except Exception as e:
        print(f"Error: {e}")