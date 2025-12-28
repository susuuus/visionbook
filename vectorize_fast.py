#!/usr/bin/env python3
"""
Fast vectorization & animation pipeline:
1. For each diagram, extract edges (Canny edge detection)
2. Vectorize edge mask to SVG using potrace
3. Create multi-layer animated GIF by rendering the SVG at increasing opacity/stroke widths
4. Export as compact GIF

Much faster than full layer-by-layer composition.
"""
import os
import subprocess
import tempfile
from pathlib import Path
from PIL import Image
import numpy as np
import cv2

DIAGRAMS = [
    "example_homography.png",
    "rotation_homography_vs3.png",
    "homography_plane_geometry2.png",
    "fig_matching_two_images3.png",
    "ransac_algo.png",
]

FIGURES_DIR = Path("figures/homography")


def extract_edges_and_create_svg(img_path, output_svg):
    """
    Extract edges from image and create SVG using potrace.
    Returns True if successful.
    """
    # Read image
    img = cv2.imread(str(img_path), cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"    Failed to read {img_path}")
        return False
    
    # Extract edges (Canny)
    edges = cv2.Canny(img, 50, 150)
    
    # Create mask suitable for potrace (invert: white edges on black background)
    mask = cv2.bitwise_not(edges)
    
    # Save as PNG, then convert to PBM for potrace
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        tmp_png = tmp.name
    
    cv2.imwrite(tmp_png, mask)
    
    # Convert PNG to PBM
    with tempfile.NamedTemporaryFile(suffix=".pbm", delete=False) as tmp:
        pbm_path = tmp.name
    
    try:
        # Use ImageMagick to convert PNG → PBM (simpler format for potrace)
        result = subprocess.run(
            ["magick", tmp_png, "-colorspace", "gray", "-threshold", "50%", pbm_path],
            capture_output=True,
            timeout=5,
        )
        
        if result.returncode != 0:
            print(f"    Failed to create PBM")
            return False
        
        # Trace to SVG
        result = subprocess.run(
            ["potrace", pbm_path, "-s", "-o", str(output_svg)],
            capture_output=True,
            text=True,
            timeout=5,
        )
        
        return result.returncode == 0
    
    finally:
        Path(tmp_png).unlink(missing_ok=True)
        Path(pbm_path).unlink(missing_ok=True)


def create_animated_gif_from_svg(svg_path, output_gif, img_size, num_frames=6):
    """
    Render SVG multiple times with increasing stroke width to create reveal animation.
    """
    width, height = img_size
    frames = []
    
    for frame_idx in range(num_frames):
        # Create temp SVG with stroke-width increase
        temp_svg = Path(tempfile.gettempdir()) / f"animated_frame_{frame_idx}.svg"
        
        # Read original SVG
        with open(svg_path, 'r') as f:
            svg_content = f.read()
        
        # Modify SVG: increase stroke width based on frame
        # This creates a "drawing" effect
        stroke_width = 0.5 + (frame_idx / num_frames) * 1.5
        
        # Simple approach: wrap paths with increased stroke
        svg_modified = svg_content.replace(
            '<path ',
            f'<path stroke="black" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round" '
        )
        
        with open(temp_svg, 'w') as f:
            f.write(svg_modified)
        
        # Render to PNG
        output_png = Path(tempfile.gettempdir()) / f"frame_{frame_idx}.png"
        result = subprocess.run(
            [
                "magick",
                "-density", "120",
                str(temp_svg),
                "-resize", f"{width}x{height}",
                "-background", "white",
                "-flatten",
                str(output_png),
            ],
            capture_output=True,
            timeout=10,
        )
        
        if result.returncode == 0:
            frames.append(Image.open(output_png))
            print(f"      Frame {frame_idx + 1}/{num_frames}")
        else:
            print(f"      Frame {frame_idx + 1} rendering failed")
        
        temp_svg.unlink(missing_ok=True)
    
    if not frames:
        return False
    
    # Create GIF
    frames[0].save(
        output_gif,
        save_all=True,
        append_images=frames[1:],
        duration=400,
        loop=0,
        optimize=True,
    )
    
    print(f"    ✓ Saved GIF: {output_gif}")
    return True


def process_diagram_fast(diagram_name):
    """Fast pipeline: extract edges → potrace → animated SVG render → GIF"""
    input_path = FIGURES_DIR / diagram_name
    base_name = diagram_name.replace(".png", "")
    output_gif = FIGURES_DIR / f"{base_name}_vector.gif"
    
    print(f"\nProcessing: {diagram_name}")
    
    if not input_path.exists():
        print(f"  Skipped: {input_path} not found")
        return None
    
    try:
        # Get image size
        img = Image.open(input_path)
        img_size = img.size
        print(f"  Image size: {img_size}")
        
        # Step 1: Extract edges and vectorize
        print("  1. Extracting edges and vectorizing...")
        with tempfile.NamedTemporaryFile(suffix=".svg", delete=False) as tmp:
            svg_path = tmp.name
        
        if not extract_edges_and_create_svg(str(input_path), svg_path):
            print("    Failed to create SVG")
            Path(svg_path).unlink(missing_ok=True)
            return None
        
        print("    ✓ SVG created")
        
        # Step 2: Create animated GIF
        print("  2. Creating animated GIF...")
        if create_animated_gif_from_svg(svg_path, output_gif, img_size, num_frames=6):
            Path(svg_path).unlink(missing_ok=True)
            return str(output_gif)
        
        Path(svg_path).unlink(missing_ok=True)
        return None
    
    except Exception as e:
        print(f"  Error: {e}")
        import traceback
        traceback.print_exc()
        return None


def main():
    """Process all diagrams."""
    print("=" * 70)
    print("FAST VECTORIZATION & EDGE-ANIMATION PIPELINE")
    print("=" * 70)
    
    results = {}
    for diagram in DIAGRAMS:
        result = process_diagram_fast(diagram)
        if result:
            results[diagram] = result
    
    print("\n" + "=" * 70)
    print(f"✓ Processed {len(results)}/{len(DIAGRAMS)} diagrams")
    print("=" * 70)
    
    if results:
        print("\nGenerated animated GIFs:")
        for orig, gif in results.items():
            gif_path = Path(gif)
            if gif_path.exists():
                size_kb = gif_path.stat().st_size / 1024
                print(f"  {orig:40s} → {gif_path.name:45s} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
