# src/nodes/renderer.py

import sys
import subprocess
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

def render(py_path: str | Path, quality: str = "l") -> Path:
    py_path = Path(py_path)
    
    subprocess.run([
        "manim", f"-q{quality}", str(py_path), "AnimatedFigure",
        "--media_dir", str(Path(py_path).parent.parent / "outputs" / "media")
    ], check=True)
    
    # manim saves to media/videos/<stem>/<res>/AnimatedFigure.mp4
    quality_map = {"l": "480p15", "m": "720p30", "h": "1080p60"}
    resolution = quality_map[quality]
    out_path = Path("media/videos") / py_path.stem / resolution / "AnimatedFigure.mp4"
    
    print(f"[renderer] Saved MP4 → {out_path}")
    return out_path

if __name__ == "__main__":
    try:
        py_path = Path('/Users/su/Documents/su/visionbook/logs.agents/src/outputs/example_homography.py')
        mp4 = render(py_path)
        print(f"MP4 at: {mp4}")
    except Exception as e:
        print(f"Error: {e}")
