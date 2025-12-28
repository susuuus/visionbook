#!/usr/bin/env python3
# Record by exporting frames as PNG images, then encode to MP4
import sys
import time
import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path('figures/neural_nets_as_data_transformations')
OUT_DIR.mkdir(parents=True, exist_ok=True)
FRAMES_DIR = OUT_DIR / 'frames_temp'
FRAMES_DIR.mkdir(exist_ok=True)
VIDEO_PATH = OUT_DIR / 'linear_demo.mp4'
URL = 'file://' + str(Path(__file__).resolve().parent.joinpath('linearOnly_hq_record.html'))
DURATION_MS = 4000
VIEWPORT_W = 1920
VIEWPORT_H = 1080
FPS = 30

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': VIEWPORT_W, 'height': VIEWPORT_H})
        page = context.new_page()
        print(f'Navigating to {URL}')
        page.goto(URL)
        # Wait for animateTransformation function
        page.wait_for_function("typeof window.animateTransformation === 'function'", timeout=5000)
        
        # Calculate total frames
        total_frames = int((DURATION_MS / 1000.0) * FPS)
        print(f'Recording {total_frames} frames at {FPS} FPS to {FRAMES_DIR}')
        
        # Export each frame as PNG
        for frame_idx in range(total_frames + 1):
            t = frame_idx / max(1, total_frames)
            page.evaluate(f"window.animateTransformation({t})")
            
            # Give renderer time to draw
            time.sleep(0.01)
            
            # Save screenshot
            frame_path = FRAMES_DIR / f'frame_{frame_idx:06d}.png'
            page.screenshot(path=str(frame_path), full_page=False)
            
            if (frame_idx + 1) % 10 == 0:
                print(f'  Saved frame {frame_idx + 1}/{total_frames + 1}')
        
        context.close()
        browser.close()
    
    print(f'\nEncoding {total_frames + 1} frames to MP4...')
    # Use ffmpeg to encode PNG frames to MP4
    cmd = [
        'ffmpeg',
        '-y',
        '-framerate', str(FPS),
        '-i', str(FRAMES_DIR / 'frame_%06d.png'),
        '-c:v', 'libx264',
        '-crf', '10',  # Very high quality
        '-preset', 'slow',
        '-pix_fmt', 'yuv420p',
        str(VIDEO_PATH)
    ]
    
    result = subprocess.run(cmd, capture_output=False)
    if result.returncode == 0:
        print(f'✓ Successfully encoded to {VIDEO_PATH}')
        # Clean up frames
        import shutil
        shutil.rmtree(FRAMES_DIR)
        print('  Cleaned up temporary frame files')
    else:
        print('✗ ffmpeg encoding failed')
        sys.exit(1)

if __name__ == '__main__':
    main()
