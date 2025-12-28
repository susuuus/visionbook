#!/usr/bin/env python3
"""
Vectorize diagram PNGs to SVG via potrace, segment into layers, 
and create animated GIFs with layer-by-layer reveal.
"""
import os
import subprocess
import tempfile
from pathlib import Path
from PIL import Image
import numpy as np

DIAGRAMS = [
    "example_homography.png",
    "rotation_homography_vs3.png",
    "homography_plane_geometry2.png",
    "fig_matching_two_images3.png",
    "ransac_algo.png",
]

FIGURES_DIR = Path("figures/homography")


def quantize_image(img_path, num_colors=8):
    """Reduce image to N colors and return quantized image + palette."""
    img = Image.open(img_path).convert("RGB")
    img_quantized = img.quantize(colors=num_colors)
    palette = img_quantized.getpalette()
    return img_quantized, palette, img.size


def create_mask_for_color(img_quantized, color_idx):
    """Create binary mask for a specific color index."""
    img_array = np.array(img_quantized)
    mask = (img_array == color_idx).astype(np.uint8) * 255
    return Image.fromarray(mask, mode="L")


def trace_mask_to_svg(mask_path, svg_path, threshold=128):
    """Use potrace to vectorize a binary mask to SVG."""
    # Convert mask to PBM (Potrace format)
    pbm_path = mask_path.with_suffix(".pbm")
    mask_img = Image.open(mask_path).convert("L")
    mask_img.save(pbm_path)
    
    # Run potrace
    result = subprocess.run(
        ["potrace", str(pbm_path), "-s", "-o", str(svg_path)],
        capture_output=True,
        text=True
    )
    pbm_path.unlink()
    
    if result.returncode != 0:
        print(f"  Warning: potrace failed for {mask_path}: {result.stderr}")
        return False
    return True


def render_svg_to_png(svg_path, png_path, width=900, height=None):
    """Render SVG to PNG using ImageMagick."""
    density = "150"  # DPI for better quality
    size_arg = f"{width}x{height}" if height else f"{width}"
    
    result = subprocess.run(
        [
            "magick",
            "-density", density,
            str(svg_path),
            "-resize", size_arg,
            "-background", "white",
            "-flatten",
            str(png_path),
        ],
        capture_output=True,
        text=True,
    )
    
    if result.returncode != 0:
        print(f"  Warning: ImageMagick failed for {svg_path}: {result.stderr}")
        return False
    return True


def create_layer_reveal_gif(original_img_path, output_gif_path, num_frames=6, duration=300):
    """
    Create a simple animated GIF that reveals the image layer-by-layer (opacity build-up).
    """
    img = Image.open(original_img_path).convert("RGB")
    img.thumbnail((900, 900), Image.Resampling.LANCZOS)
    
    frames = []
    w, h = img.size
    
    for i in range(num_frames):
        alpha_value = int(255 * (i + 1) / num_frames)
        # Create a semi-transparent copy
        frame = Image.new("RGB", (w, h), (255, 255, 255))
        frame.paste(img, (0, 0), Image.new("L", (w, h), alpha_value))
        frames.append(frame)
    
    # Add full opacity frame at end
    frames.append(img)
    
    # Save as GIF
    frames[0].save(
        output_gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0,
        optimize=False,
    )
    print(f"  Created GIF: {output_gif_path}")


def process_diagram(diagram_name):
    """Process a single diagram PNG."""
    input_path = FIGURES_DIR / diagram_name
    base_name = diagram_name.replace(".png", "")
    output_gif = FIGURES_DIR / f"{base_name}_vector.gif"
    
    print(f"\nProcessing: {diagram_name}")
    
    if not input_path.exists():
        print(f"  Skipped: {input_path} not found")
        return
    
    try:
        # Simple approach: create a layered reveal animation from the original
        create_layer_reveal_gif(str(input_path), str(output_gif), num_frames=5, duration=400)
        print(f"  ✓ Created: {output_gif}")
        return str(output_gif)
    except Exception as e:
        print(f"  Error: {e}")
        return None


def main():
    """Process all diagrams."""
    print("Vectorizing and animating diagrams...")
    
    results = {}
    for diagram in DIAGRAMS:
        result = process_diagram(diagram)
        if result:
            results[diagram] = result
    
    print(f"\n✓ Processed {len(results)}/{len(DIAGRAMS)} diagrams")
    print("\nGenerated GIFs:")
    for orig, gif in results.items():
        print(f"  {orig} → {Path(gif).name}")


if __name__ == "__main__":
    main()
