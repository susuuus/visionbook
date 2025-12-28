#!/usr/bin/env python3
"""
Proper vectorization pipeline:
1. Quantize PNG to limited color palette
2. For each color layer: create mask → potrace to SVG
3. Parse SVG paths, group by color
4. Build keyframed animation (elements appear in sequence)
5. Render frames to PNG, export as GIF

This creates true segmented, layered animations.
"""
import os
import subprocess
import tempfile
from pathlib import Path
from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET
import numpy as np

DIAGRAMS = [
    "example_homography.png",
    "rotation_homography_vs3.png",
    "homography_plane_geometry2.png",
    "fig_matching_two_images3.png",
    "ransac_algo.png",
]

FIGURES_DIR = Path("figures/homography")


def quantize_to_colors(img_path, num_colors=6):
    """Quantize image to N colors, return (quantized_img, color_palette)."""
    img = Image.open(img_path).convert("RGB")
    img_quantized = img.quantize(colors=num_colors)
    return img_quantized, img.size


def get_color_regions(img_quantized):
    """
    Extract connected components per color.
    Returns dict: {color_idx: [bounding_boxes]}
    """
    img_array = np.array(img_quantized)
    unique_colors = np.unique(img_array)
    
    regions = {}
    for color_idx in unique_colors:
        mask = (img_array == color_idx).astype(np.uint8)
        if mask.sum() > 50:  # Only consider regions with >50 pixels
            regions[int(color_idx)] = mask
    
    return regions


def create_mask_image(mask_array, size):
    """Create PIL Image from binary mask array."""
    mask_img = Image.fromarray((mask_array * 255).astype(np.uint8), mode="L")
    return mask_img


def mask_to_svg(mask_img, svg_path):
    """
    Convert binary mask to SVG using potrace.
    Returns True if successful.
    """
    with tempfile.NamedTemporaryFile(suffix=".pbm", delete=False) as pbm_file:
        pbm_path = pbm_file.name
    
    try:
        # Save mask as PBM
        mask_img.save(pbm_path)
        
        # Trace to SVG
        result = subprocess.run(
            ["potrace", pbm_path, "-s", "-o", str(svg_path)],
            capture_output=True,
            text=True,
            timeout=10,
        )
        
        return result.returncode == 0
    finally:
        if Path(pbm_path).exists():
            Path(pbm_path).unlink()


def parse_svg_paths(svg_path):
    """Extract all <path> elements from SVG."""
    try:
        tree = ET.parse(svg_path)
        root = tree.getroot()
        paths = []
        
        # Handle namespace
        ns = {'svg': 'http://www.w3.org/2000/svg'}
        for path_elem in root.findall('.//svg:path', ns):
            d = path_elem.get('d')
            if d:
                paths.append(d)
        
        return paths
    except Exception as e:
        print(f"    Error parsing SVG: {e}")
        return []


def create_keyframed_svg(svg_path, output_frames, width, height, num_frames=4):
    """
    Load SVG, split paths into groups, and create keyframed PNG frames.
    Each frame reveals more paths.
    """
    paths = parse_svg_paths(svg_path)
    
    if not paths:
        print(f"    No paths found in {svg_path}")
        return False
    
    paths_per_frame = max(1, len(paths) // num_frames)
    frames = []
    
    for frame_idx in range(num_frames):
        # Create a temporary SVG with subset of paths
        temp_svg = Path(tempfile.gettempdir()) / f"frame_{frame_idx}.svg"
        
        # Determine which paths to include
        num_paths = min((frame_idx + 1) * paths_per_frame, len(paths))
        subset_paths = paths[:num_paths]
        
        # Build SVG with these paths
        svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="{width}" height="{height}" fill="white"/>
'''
        for path_d in subset_paths:
            svg_content += f'  <path d="{path_d}" fill="black" stroke="none"/>\n'
        svg_content += '</svg>'
        
        with open(temp_svg, 'w') as f:
            f.write(svg_content)
        
        # Render to PNG using ImageMagick
        output_png = output_frames / f"frame_{frame_idx}.png"
        result = subprocess.run(
            [
                "magick",
                "-density", "150",
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
            frames.append(output_png)
            print(f"      Frame {frame_idx + 1}/{num_frames}")
        
        temp_svg.unlink(missing_ok=True)
    
    return frames


def frames_to_gif(frame_paths, output_gif, duration=500, loop=0):
    """Create animated GIF from sequence of PNG frames."""
    if not frame_paths:
        print(f"    No frames to create GIF")
        return False
    
    # Load frames as PIL Images
    images = [Image.open(str(f)) for f in sorted(frame_paths)]
    
    # Save as animated GIF
    images[0].save(
        output_gif,
        save_all=True,
        append_images=images[1:],
        duration=duration,
        loop=loop,
        optimize=False,
    )
    
    print(f"    ✓ GIF saved: {output_gif}")
    return True


def process_diagram_proper(diagram_name):
    """
    Full pipeline: quantize → mask per color → potrace → keyframed SVG → PNG frames → GIF
    """
    input_path = FIGURES_DIR / diagram_name
    base_name = diagram_name.replace(".png", "")
    output_gif = FIGURES_DIR / f"{base_name}_vector.gif"
    
    print(f"\nProcessing: {diagram_name}")
    
    if not input_path.exists():
        print(f"  Skipped: {input_path} not found")
        return None
    
    try:
        # Step 1: Quantize
        print("  1. Quantizing to color palette...")
        img_quantized, img_size = quantize_to_colors(str(input_path), num_colors=8)
        
        # Step 2: Get color regions
        print("  2. Extracting color regions...")
        regions = get_color_regions(img_quantized)
        
        if not regions:
            print("    No significant regions found")
            return None
        
        print(f"    Found {len(regions)} color regions")
        
        # Step 3: Create SVG for largest region (or combine)
        print("  3. Vectorizing regions with potrace...")
        
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)
            svg_paths = []
            
            for color_idx, mask in sorted(regions.items(), 
                                         key=lambda x: x[1].sum(), 
                                         reverse=True)[:3]:  # Top 3 regions
                mask_img = create_mask_image(mask, img_size)
                svg_path = tmpdir_path / f"color_{color_idx}.svg"
                
                if mask_to_svg(mask_img, svg_path):
                    svg_paths.append(svg_path)
                    print(f"    ✓ Vectorized color {color_idx}")
            
            if not svg_paths:
                print("    Failed to vectorize any regions")
                return None
            
            # Step 4: Create keyframed frames
            print("  4. Creating keyframed animation frames...")
            frames_dir = tmpdir_path / "frames"
            frames_dir.mkdir()
            
            frame_pngs = []
            for svg_p in svg_paths:
                frames = create_keyframed_svg(
                    svg_p, frames_dir, 
                    img_size[0], img_size[1], 
                    num_frames=4
                )
                frame_pngs.extend(frames)
            
            if not frame_pngs:
                print("    Failed to create animation frames")
                return None
            
            # Step 5: Create GIF
            print("  5. Creating animated GIF...")
            if frames_to_gif(frame_pngs, output_gif, duration=600, loop=0):
                return str(output_gif)
    
    except Exception as e:
        print(f"  Error: {e}")
        import traceback
        traceback.print_exc()
    
    return None


def main():
    """Process all diagrams."""
    print("=" * 60)
    print("PROPER VECTORIZATION & ANIMATION PIPELINE")
    print("=" * 60)
    
    results = {}
    for diagram in DIAGRAMS:
        result = process_diagram_proper(diagram)
        if result:
            results[diagram] = result
    
    print("\n" + "=" * 60)
    print(f"✓ Processed {len(results)}/{len(DIAGRAMS)} diagrams")
    print("=" * 60)
    
    if results:
        print("\nGenerated animated GIFs:")
        for orig, gif in results.items():
            gif_path = Path(gif)
            size_mb = gif_path.stat().st_size / (1024 * 1024)
            print(f"  {orig:40s} → {gif_path.name:45s} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
