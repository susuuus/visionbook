#!/usr/bin/env python3
# Headless recorder using Playwright Python
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

OUT_DIR = Path('figures/neural_nets_as_data_transformations')
OUT_DIR.mkdir(parents=True, exist_ok=True)
VIDEO_PREFIX = OUT_DIR / 'linear_demo'
from pathlib import PurePosixPath
URL = 'file://' + str(Path(__file__).resolve().parent.joinpath('linearOnly_hq_record.html'))
DURATION_MS = 4000
VIEWPORT_W = 1920
VIEWPORT_H = 1080

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Record at native 1920x1080 resolution
        context = browser.new_context(record_video_dir=str(OUT_DIR), viewport={'width': VIEWPORT_W, 'height': VIEWPORT_H})
        page = context.new_page()
        print(f'Navigating to {URL}')
        page.goto(URL)
        # Wait for animateTransformation function to be available
        page.wait_for_function("typeof window.animateTransformation === 'function'", timeout=5000)
        print('Animating transformation (headless)')
        # Run animation with 60 frames
        steps = 60
        for i in range(steps + 1):
            t = i / steps
            page.evaluate(f"window.animateTransformation({t})")
            time.sleep((DURATION_MS / steps) / 1000.0)
        # Small buffer to ensure final frame is captured
        time.sleep(0.5)
        # Close context to flush the recording
        print('Closing context to finalize video...')
        context.close()
        browser.close()

        # Find the produced .webm video file in OUT_DIR
        video_files = list(OUT_DIR.glob('*.webm'))
        if not video_files:
            print('No webm video found in', OUT_DIR)
            sys.exit(1)
        latest = max(video_files, key=lambda p: p.stat().st_mtime)
        print('Recorded webm at', latest)
        # Rename/move to linear_demo.webm
        target_webm = VIDEO_PREFIX.with_suffix('.webm')
        if latest != target_webm:
            latest.replace(target_webm)
        print('Saved recording as', target_webm)
        print('Done')

if __name__ == '__main__':
    main()
