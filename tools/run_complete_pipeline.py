#!/usr/bin/env python3
"""
COMPLETE WORKING PIPELINE
Properly classifies and generates 3D figures using proven templates
"""

import json
import shutil
from pathlib import Path
from PIL import Image
import numpy as np

# Use the proven working classifier
exec(open('tools/figure_pipeline_2stage.py').read().split('class Figure3DGenerator')[0])

def main():
    """Complete pipeline with working templates"""
    figures_dir = Path("figures/imaging")
    output_dir = Path("interactive_figures/imaging")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("="*70)
    print("COMPLETE 3D FIGURE GENERATION PIPELINE")
    print("="*70)
    
    # STAGE 1: Classification
    print("\n📊 STAGE 1: Classifying figures...")
    print("-" * 70)
    classifier = FigureClassifier(figures_dir)
    classifications = classifier.classify_all()
    
    # Filter for 3D diagrams only
    diagrams_3d = [c for c in classifications if c['category'] == '3d_diagram' and c['confidence'] >= 0.7]
    
    print(f"\nFound {len(diagrams_3d)} 3D diagrams:")
    for c in diagrams_3d:
        print(f"  ✓ {c['file']:<40} → {c['subcategory']}")
    
    # STAGE 2: Generation with proven templates
    print(f"\n🔨 STAGE 2: Generating visualizations...")
    print("-" * 70)
    
    # Template mapping to proven working files
    template_map = {
        'brdf.png': {
            'source': '/Users/su/Downloads/light_surface_3d (10).html',
            'output': 'fig-lightSpray_3d.html',
            'title': 'Light-Surface Interaction (BRDF)'
        },
        'no_picture_on_a_wall_aina.png': {
            'source': '/Users/su/Desktop/AI Augmented Book/Interactive Figures/pinhole.html',
            'output': 'fig-wallpicture_3d.html',
            'title': 'Pinhole Camera - Wall Picture'
        },
        'similar_triangles2.png': {
            'generate': 'similar_triangles',
            'output': 'fig-pinholeGeometry2_3d.html'
        },
        'pinhole_names2.png': {
            'generate': 'camera_coordinates',
            'output': 'fig-pinhole-names2_3d.html'
        },
        'pinhole_geometry2.png': {
            'generate': 'pinhole_projection',
            'output': 'fig-pinholeGeometry_3d.html'
        },
        'orthogonal_projection.png': {
            'generate': 'orthographic',
            'output': 'fig-orthographics_3d.html'
        }
    }
    
    generated = []
    skipped = []
    
    for c in diagrams_3d:
        filename = c['file']
        print(f"\n{filename}")
        
        if filename in template_map:
            spec = template_map[filename]
            output_path = output_dir / spec['output']
            
            try:
                if 'source' in spec:
                    # Copy from proven template
                    source = Path(spec['source'])
                    if source.exists():
                        with open(source, 'r') as f:
                            content = f.read()
                        # Update title
                        content = content.replace('<title>Fig 5.3 (b) Pinhole Camera</title>', 
                                                f'<title>{spec["title"]}</title>')
                        content = content.replace('<title>Light-Surface Interaction</title>',
                                                f'<title>{spec["title"]}</title>')
                        with open(output_path, 'w') as f:
                            f.write(content)
                        print(f"  ✓ Copied from template → {output_path.name}")
                        generated.append(str(output_path))
                    else:
                        print(f"  ✗ Template not found: {source}")
                        skipped.append(filename)
                
                elif 'generate' in spec:
                    # Use fixed generation (from generate_imaging_3d_fixed.py)
                    if spec['generate'] == 'similar_triangles':
                        from tools.generate_imaging_3d_fixed import generate_similar_triangles_fixed
                        generate_similar_triangles_fixed(output_path)
                        print(f"  ✓ Generated → {output_path.name}")
                        generated.append(str(output_path))
                    elif spec['generate'] == 'camera_coordinates':
                        from tools.generate_imaging_3d_fixed import generate_camera_coordinates_html
                        generate_camera_coordinates_html(output_path)
                        print(f"  ✓ Generated → {output_path.name}")
                        generated.append(str(output_path))
                    else:
                        # Use existing working versions
                        existing = output_dir / spec['output']
                        if existing.exists():
                            print(f"  ✓ Already exists → {existing.name}")
                            generated.append(str(existing))
                        else:
                            print(f"  ⚠ Generator not implemented: {spec['generate']}")
                            skipped.append(filename)
                            
            except Exception as e:
                print(f"  ✗ Error: {e}")
                skipped.append(filename)
        else:
            print(f"  ⚠ No template mapping")
            skipped.append(filename)
    
    # Summary
    print(f"\n{'='*70}")
    print(f"📈 SUMMARY")
    print("="*70)
    print(f"✓ Generated: {len(generated)} visualizations")
    print(f"⚠ Skipped: {len(skipped)} figures")
    
    if generated:
        print(f"\n✅ Successfully generated:")
        for g in generated:
            print(f"  - {Path(g).name}")
    
    if skipped:
        print(f"\n⏭️  Skipped (no template):")
        for s in skipped[:5]:
            print(f"  - {s}")
        if len(skipped) > 5:
            print(f"  ... and {len(skipped) - 5} more")
    
    print(f"\n🌐 View at: http://localhost:8000/interactive_figures/imaging/")
    print("="*70)

if __name__ == '__main__':
    main()
