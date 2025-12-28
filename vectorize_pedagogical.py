#!/usr/bin/env python3
"""
Concept-driven color segmentation & animation pipeline.

For each diagram, define pedagogical animation order that explains the concept:
- rotation_homography_vs3: show camera1 → rotation → camera2 (left → right)
- example_homography: show input grid → arrow → output distorted (left → right)
- homography_plane_geometry2: show plane → camera → projection (bottom-up or top-down)
- ransac_algo: show initial points → fits → best fit (procedural)
- fig_matching_two_images3: show left image → matches → right image (left → right)
"""
import os
import subprocess
import tempfile
from pathlib import Path
from PIL import Image, ImageDraw
import numpy as np
from scipy import ndimage
import cv2

FIGURES_DIR = Path("figures/homography")

# Define pedagogical animation order for each diagram
ANIMATION_SEQUENCES = {
    "rotation_homography_vs3.png": {
        "description": "Camera rotation: show left camera → rotation arrow → right camera",
        "spatial_order": "left_to_right",  # Animate left side first, then right
        "animation_frames": 5,
    },
    "example_homography.png": {
        "description": "Grid homography: show input grid → transformation arrow → output grid",
        "spatial_order": "left_to_right",
        "animation_frames": 4,
    },
    "homography_plane_geometry2.png": {
        "description": "Planar projection: show plane → camera setup",
        "spatial_order": "bottom_to_top",  # Plane at bottom, camera above
        "animation_frames": 4,
    },
    "fig_matching_two_images3.png": {
        "description": "Feature matching: left image → correspondence lines → right image",
        "spatial_order": "left_to_right",
        "animation_frames": 4,
    },
    "ransac_algo.png": {
        "description": "RANSAC algorithm: show points → intermediate fits → final line",
        "spatial_order": "top_to_bottom",  # Steps progress downward typically
        "animation_frames": 5,
    },
}


def quantize_image(img_path, num_colors=8):
    """Quantize image to limited color palette."""
    img = Image.open(img_path).convert("RGB")
    img_quantized = img.quantize(colors=num_colors)
    return img_quantized, img.size


def extract_color_blocks(img_quantized, min_block_size=200):
    """
    Extract connected components (color blocks) from quantized image.
    Returns dict: {color_idx: [(y_range, x_range, centroid_x, centroid_y)]}
    """
    img_array = np.array(img_quantized)
    blocks = {}
    
    for color_idx in np.unique(img_array):
        mask = (img_array == color_idx).astype(np.uint8)
        
        # Only keep reasonably large blocks
        if mask.sum() < min_block_size:
            continue
        
        # Find connected components
        labeled, num_features = ndimage.label(mask)
        
        for component_idx in range(1, num_features + 1):
            component_mask = (labeled == component_idx)
            
            if component_mask.sum() < min_block_size:
                continue
            
            # Get bounding box and centroid
            y_coords, x_coords = np.where(component_mask)
            y_min, y_max = y_coords.min(), y_coords.max()
            x_min, x_max = x_coords.min(), x_coords.max()
            centroid_x = x_coords.mean()
            centroid_y = y_coords.mean()
            
            if color_idx not in blocks:
                blocks[color_idx] = []
            
            blocks[color_idx].append({
                'mask': component_mask,
                'y_range': (y_min, y_max),
                'x_range': (x_min, x_max),
                'centroid': (centroid_x, centroid_y),
                'area': component_mask.sum(),
            })
    
    return blocks


def sort_blocks_pedagogically(blocks, spatial_order):
    """
    Sort blocks in pedagogical order based on diagram's teaching flow.
    
    spatial_order can be:
    - 'left_to_right': sort by x centroid
    - 'right_to_left': sort by x (reverse)
    - 'top_to_bottom': sort by y centroid
    - 'bottom_to_top': sort by y (reverse)
    - 'largest_first': by area
    """
    all_blocks = []
    for color_idx, color_blocks in blocks.items():
        for block in color_blocks:
            all_blocks.append((color_idx, block))
    
    if spatial_order == "left_to_right":
        all_blocks.sort(key=lambda x: x[1]['centroid'][0])
    elif spatial_order == "right_to_left":
        all_blocks.sort(key=lambda x: x[1]['centroid'][0], reverse=True)
    elif spatial_order == "top_to_bottom":
        all_blocks.sort(key=lambda x: x[1]['centroid'][1])
    elif spatial_order == "bottom_to_top":
        all_blocks.sort(key=lambda x: x[1]['centroid'][1], reverse=True)
    elif spatial_order == "largest_first":
        all_blocks.sort(key=lambda x: x[1]['area'], reverse=True)
    
    return all_blocks


def create_animation_frames(img_quantized, sorted_blocks, img_size, num_frames, diagram_name):
    """
    Create animation frames where blocks appear progressively.
    """
    frames = []
    h, w = img_quantized.size[1], img_quantized.size[0]
    
    # Create white background
    base_frame = Image.new("RGB", img_quantized.size, (255, 255, 255))
    
    # Recolor the quantized image
    palette = img_quantized.getpalette()
    colors = {}
    for i in range(0, len(palette), 3):
        colors[i // 3] = (palette[i], palette[i+1], palette[i+2])
    
    # Accumulate blocks frame by frame
    accumulated_mask = np.zeros((h, w), dtype=bool)
    
    blocks_per_frame = max(1, len(sorted_blocks) // num_frames)
    
    for frame_idx in range(num_frames):
        # Determine which blocks to show
        num_blocks_to_show = min((frame_idx + 1) * blocks_per_frame, len(sorted_blocks))
        
        # Accumulate masks
        accumulated_mask.fill(False)
        for block_idx in range(num_blocks_to_show):
            color_idx, block = sorted_blocks[block_idx]
            accumulated_mask |= block['mask']
        
        # Create frame: white background + colored blocks
        frame = base_frame.copy()
        frame_array = np.array(frame)
        
        # Apply accumulated mask (color all blocks shown so far)
        for block_idx in range(num_blocks_to_show):
            color_idx, block = sorted_blocks[block_idx]
            color = colors.get(color_idx, (0, 0, 0))
            frame_array[block['mask']] = color
        
        frame = Image.fromarray(frame_array)
        frames.append(frame)
        print(f"    Frame {frame_idx + 1}/{num_frames}: showing {num_blocks_to_show}/{len(sorted_blocks)} blocks")
    
    return frames


def frames_to_gif(frames, output_gif, duration=600):
    """Create GIF from frames."""
    if not frames:
        return False
    
    frames[0].save(
        output_gif,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0,
        optimize=True,
    )
    print(f"    ✓ Saved GIF: {output_gif.name}")
    return True


def process_diagram_pedagogical(diagram_name):
    """Process a diagram with pedagogical animation."""
    input_path = FIGURES_DIR / diagram_name
    base_name = diagram_name.replace(".png", "")
    output_gif = FIGURES_DIR / f"{base_name}_vector.gif"
    
    print(f"\nProcessing: {diagram_name}")
    
    if diagram_name not in ANIMATION_SEQUENCES:
        print(f"  Skipped: no animation sequence defined")
        return None
    
    seq = ANIMATION_SEQUENCES[diagram_name]
    print(f"  Strategy: {seq['description']}")
    
    try:
        # Step 1: Quantize
        print("  1. Quantizing to color palette...")
        img_quantized, img_size = quantize_image(str(input_path), num_colors=10)
        
        # Step 2: Extract color blocks
        print("  2. Extracting color blocks...")
        blocks = extract_color_blocks(img_quantized, min_block_size=150)
        total_blocks = sum(len(b) for b in blocks.values())
        print(f"    Found {total_blocks} blocks across {len(blocks)} color regions")
        
        if total_blocks < 2:
            print("    Too few blocks for animation")
            return None
        
        # Step 3: Sort pedagogically
        print(f"  3. Sorting blocks by: {seq['spatial_order']}")
        sorted_blocks = sort_blocks_pedagogically(blocks, seq['spatial_order'])
        
        # Step 4: Create animation frames
        print(f"  4. Creating {seq['animation_frames']} animation frames...")
        frames = create_animation_frames(
            img_quantized, sorted_blocks, img_size, 
            seq['animation_frames'], diagram_name
        )
        
        # Step 5: Create GIF
        print("  5. Creating GIF...")
        if frames_to_gif(frames, output_gif, duration=700):
            return str(output_gif)
    
    except Exception as e:
        print(f"  Error: {e}")
        import traceback
        traceback.print_exc()
    
    return None


def main():
    """Process all diagrams."""
    print("=" * 70)
    print("PEDAGOGICAL COLOR SEGMENTATION & ANIMATION")
    print("=" * 70)
    
    results = {}
    for diagram_name in sorted(ANIMATION_SEQUENCES.keys()):
        result = process_diagram_pedagogical(diagram_name)
        if result:
            results[diagram_name] = result
    
    print("\n" + "=" * 70)
    print(f"✓ Processed {len(results)}/{len(ANIMATION_SEQUENCES)} diagrams")
    print("=" * 70)
    
    if results:
        print("\nGenerated pedagogical animated GIFs:")
        for orig, gif in results.items():
            gif_path = Path(gif)
            if gif_path.exists():
                size_kb = gif_path.stat().st_size / 1024
                print(f"  {orig:40s} → {size_kb:7.1f} KB")


if __name__ == "__main__":
    main()
