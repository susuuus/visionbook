#!/usr/bin/env python3
"""
Extend pipeline to any chapter
Usage: python tools/extend_to_chapter.py <chapter_name>
"""

import sys
from pathlib import Path

CHAPTER_CONFIGS = {
    'lenses': {
        'figures': [
            ('lensrays1.png', 'pinhole_projection'),
            ('lensrays2.png', 'pinhole_projection'),
            ('circleOfConfusion.png', 'depth_of_field'),
        ]
    },
    'multiview': {
        'figures': [
            # Add multiview specific figures
        ]
    },
    'motion': {
        'figures': [
            # Add motion specific figures
        ]
    }
}

def setup_chapter(chapter_name: str):
    """Set up 3D pipeline for a new chapter"""
    
    figures_dir = Path(f"figures/{chapter_name}")
    if not figures_dir.exists():
        print(f"❌ Chapter figures not found: {figures_dir}")
        return
    
    output_dir = Path(f"interactive_figures/{chapter_name}")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"📁 Processing chapter: {chapter_name}")
    print(f"   Figures: {figures_dir}")
    print(f"   Output: {output_dir}")
    print()
    
    # List all figures
    all_figs = sorted(figures_dir.glob("*.png"))
    print(f"Found {len(all_figs)} PNG figures")
    
    # Show potential 3D candidates
    keywords_3d = ['geometry', 'projection', 'coordinate', 'ray', 
                   'perspective', 'camera', 'lens', 'diagram']
    
    candidates = []
    for fig in all_figs:
        if any(kw in fig.stem.lower() for kw in keywords_3d):
            candidates.append(fig.name)
    
    if candidates:
        print(f"\n🎯 Potential 3D candidates ({len(candidates)}):")
        for c in candidates[:10]:
            print(f"   - {c}")
        if len(candidates) > 10:
            print(f"   ... and {len(candidates)-10} more")
    
    print(f"\n💡 Next steps:")
    print(f"   1. Review figures in: {figures_dir}")
    print(f"   2. Identify geometric diagrams suitable for 3D")
    print(f"   3. Create templates or copy existing ones")
    print(f"   4. Update CHAPTER_CONFIGS in this script")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python tools/extend_to_chapter.py <chapter_name>")
        print("\nAvailable chapters:")
        for chapter in ['lenses', 'multiview', 'motion', 'optical_flow', 
                       'convolutional_neural_nets', 'backpropagation']:
            fdir = Path(f"figures/{chapter}")
            if fdir.exists():
                print(f"  - {chapter}")
        sys.exit(1)
    
    setup_chapter(sys.argv[1])
