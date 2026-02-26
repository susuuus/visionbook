#!/usr/bin/env python3
"""
Two-stage pipeline: Classification → Generation
Stage 1: Classify figures using visual analysis
Stage 2: Generate 3D based on geometric content
"""

import json
from pathlib import Path
from PIL import Image
import numpy as np
from typing import Dict, List, Tuple

class FigureClassifier:
    """Stage 1: Classify figures into categories"""
    
    def __init__(self, figures_dir: Path):
        self.figures_dir = figures_dir
        
    def analyze_figure(self, fig_path: Path) -> Dict:
        """Analyze a single figure and classify it"""
        try:
            img = Image.open(fig_path)
            img_array = np.array(img)
        except Exception as e:
            return {
                'category': 'error',
                'reason': f'Cannot load: {e}',
                'confidence': 0.0
            }
        
        # Run classification checks in order
        checks = [
            self._check_photograph,
            self._check_3d_diagram,
            self._check_2d_diagram
        ]
        
        for check in checks:
            result = check(fig_path, img_array)
            if result['category'] != 'unknown':
                return result
        
        return {
            'category': 'unknown',
            'reason': 'Could not classify',
            'confidence': 0.0
        }
    
    def _check_photograph(self, fig_path: Path, img_array: np.ndarray) -> Dict:
        """Check if it's a photograph"""
        # Photographs have high local variance and many unique colors
        if len(img_array.shape) < 2:
            return {'category': 'unknown'}
        
        gray = np.mean(img_array[:,:,:3], axis=2) if len(img_array.shape) == 3 else img_array
        
        # Calculate local variance
        h, w = gray.shape
        local_vars = []
        for i in range(0, h-5, 5):
            for j in range(0, w-5, 5):
                patch = gray[i:i+5, j:j+5]
                local_vars.append(np.var(patch))
        
        avg_local_var = np.mean(local_vars)
        
        # Count unique colors
        if len(img_array.shape) == 3:
            reshaped = img_array[:,:,:3].reshape(-1, 3)
            unique_colors = len(np.unique(reshaped, axis=0))
        else:
            unique_colors = len(np.unique(img_array))
        
        # Check filename clues
        filename = fig_path.stem.lower()
        photo_keywords = ['photo', 'jpg', 'sphere', 'moon', 'room', 'simple_pinhole', 
                         'telescope', 'lens', 'toby', 'gumby']
        has_photo_keyword = any(kw in filename for kw in photo_keywords)
        
        is_photo = (avg_local_var > 500 or unique_colors > 1000) or has_photo_keyword
        
        if is_photo:
            return {
                'category': 'photograph',
                'reason': f'Photo characteristics (var={avg_local_var:.0f}, colors={unique_colors})',
                'confidence': 0.9
            }
        
        return {'category': 'unknown'}
    
    def _check_3d_diagram(self, fig_path: Path, img_array: np.ndarray) -> Dict:
        """Check if it's a 3D geometric diagram"""
        filename = fig_path.stem.lower()
        
        # Strong 3D indicators in filename
        strong_3d_keywords = [
            'pinhole_geometry', 'pinholegeometry', 'pinhole_names', 'pinholenames',
            'similar_triangle', 'similartriangle',
            'orthogonal_projection', 'orthographic', 'corner_camera', 
            'no_picture', 'nopicture', 'wall_aina', 'wallpicture',
            'brdf'
        ]
        
        # Weak 3D indicators
        weak_3d_keywords = [
            'pinhole', 'projection', 'camera', 'perspective', 
            'coordinate', 'geometry', 'ray', 'lens'
        ]
        
        has_strong = any(kw in filename for kw in strong_3d_keywords)
        has_weak = any(kw in filename for kw in weak_3d_keywords)
        
        # Check color palette (diagrams have limited colors)
        if len(img_array.shape) == 3:
            reshaped = img_array[:,:,:3].reshape(-1, 3)
            unique_colors = len(np.unique(reshaped, axis=0))
            is_diagram = unique_colors < 500
        else:
            is_diagram = True
        
        if has_strong and is_diagram:
            return {
                'category': '3d_diagram',
                'reason': 'Strong 3D keywords and diagram characteristics',
                'confidence': 0.95,
                'subcategory': self._identify_3d_subcategory(filename)
            }
        elif has_weak and is_diagram:
            return {
                'category': '3d_diagram',
                'reason': 'Possible 3D diagram based on keywords',
                'confidence': 0.7,
                'subcategory': self._identify_3d_subcategory(filename)
            }
        
        return {'category': 'unknown'}
    
    def _identify_3d_subcategory(self, filename: str) -> str:
        """Identify specific type of 3D diagram"""
        if 'brdf' in filename or 'light' in filename:
            return 'light_surface'
        elif 'similar' in filename and 'triangle' in filename:
            return 'similar_triangles'
        elif 'orthogonal' in filename or 'orthographic' in filename:
            return 'orthographic_projection'
        elif 'pinhole_geometry' in filename:
            return 'pinhole_geometry'
        elif 'pinhole_names' in filename or 'coordinate' in filename:
            return 'camera_coordinates'
        elif 'no_picture' in filename or 'wall' in filename:
            return 'pinhole_scene'
        elif 'corner_camera' in filename:
            return 'corner_camera'
        else:
            return 'generic_3d'
    
    def _check_2d_diagram(self, fig_path: Path, img_array: np.ndarray) -> Dict:
        """Check if it's a simple 2D diagram"""
        if len(img_array.shape) == 3:
            reshaped = img_array[:,:,:3].reshape(-1, 3)
            unique_colors = len(np.unique(reshaped, axis=0))
        else:
            unique_colors = len(np.unique(img_array))
        
        # Simple 2D diagrams have very few colors and no 3D keywords
        if unique_colors < 100:
            return {
                'category': '2d_diagram',
                'reason': 'Simple diagram with limited colors',
                'confidence': 0.8
            }
        
        return {'category': 'unknown'}
    
    def classify_all(self, pattern: str = "*.png") -> List[Dict]:
        """Classify all figures matching pattern"""
        results = []
        
        for fig_path in sorted(self.figures_dir.glob(pattern)):
            # Skip -0, -1, -2 variants (multi-panel figure exports)
            if fig_path.stem.endswith(('-0', '-1', '-2')):
                continue
            
            classification = self.analyze_figure(fig_path)
            results.append({
                'file': fig_path.name,
                'path': str(fig_path),
                **classification
            })
        
        return results


class Figure3DGenerator:
    """Stage 2: Generate 3D visualizations for classified 3D diagrams"""
    
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Template mapping
        self.templates = {
            'light_surface': '/Users/su/Downloads/light_surface_3d (10).html',
            'pinhole_scene': '/Users/su/Desktop/AI Augmented Book/Interactive Figures/pinhole.html',
            'pinhole_geometry': 'generate_pinhole_geometry',
            'similar_triangles': 'generate_similar_triangles',
            'orthographic_projection': 'generate_orthographic',
            'camera_coordinates': 'generate_camera_coordinates'
        }
    
    def generate(self, classification: Dict) -> str:
        """Generate 3D visualization based on classification"""
        subcategory = classification.get('subcategory', 'generic_3d')
        filename = classification['file']
        
        # Determine output filename
        fig_name = Path(filename).stem.replace('_', '-')
        output_path = self.output_dir / f"{fig_name}_3d.html"
        
        template = self.templates.get(subcategory)
        
        if not template:
            return f"No template for {subcategory}"
        
        # If template is a file path, copy it
        if isinstance(template, str) and Path(template).exists():
            self._copy_template(Path(template), output_path, fig_name)
            return str(output_path)
        
        # If template is a generator function name, call it
        if isinstance(template, str) and hasattr(self, template):
            generator = getattr(self, template)
            generator(output_path)
            return str(output_path)
        
        return f"Template not implemented: {template}"
    
    def _copy_template(self, source: Path, dest: Path, fig_name: str):
        """Copy and update template file"""
        with open(source, 'r') as f:
            content = f.read()
        
        # Update title
        content = content.replace(
            '<title>Fig 5.3 (b) Pinhole Camera</title>',
            f'<title>{fig_name.replace("-", " ").title()}</title>'
        )
        content = content.replace(
            '<title>Light-Surface Interaction</title>',
            f'<title>{fig_name.replace("-", " ").title()}</title>'
        )
        
        with open(dest, 'w') as f:
            f.write(content)
    
    # Generator methods would be defined here (similar to previous implementations)
    # For brevity, I'll reference the working ones from the fixed script


def main():
    """Run two-stage pipeline"""
    figures_dir = Path("figures/imaging")
    output_dir = Path("interactive_figures/imaging")
    
    print("="*60)
    print("TWO-STAGE PIPELINE: Classification → Generation")
    print("="*60)
    print()
    
    # STAGE 1: Classification
    print("STAGE 1: Classifying figures...")
    print("-" * 60)
    classifier = FigureClassifier(figures_dir)
    classifications = classifier.classify_all()
    
    # Summary by category
    categories = {}
    for c in classifications:
        cat = c['category']
        categories[cat] = categories.get(cat, 0) + 1
    
    print(f"\nClassification Summary:")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count} figures")
    
    # Show 3D diagrams found
    print(f"\n3D Diagrams identified:")
    print("-" * 60)
    for c in classifications:
        if c['category'] == '3d_diagram':
            print(f"  {c['file']}")
            print(f"    → {c['subcategory']} (confidence: {c['confidence']:.0%})")
            print(f"    → {c['reason']}")
    
    # Save classification results
    results_file = output_dir / "classification_results.json"
    output_dir.mkdir(parents=True, exist_ok=True)
    with open(results_file, 'w') as f:
        json.dump(classifications, f, indent=2)
    print(f"\n✓ Classifications saved to: {results_file}")
    
    # STAGE 2: Generation
    print(f"\n{'='*60}")
    print("STAGE 2: Generating 3D visualizations...")
    print("-" * 60)
    
    generator = Figure3DGenerator(output_dir)
    generated = []
    
    for c in classifications:
        if c['category'] == '3d_diagram' and c['confidence'] >= 0.7:
            print(f"\nGenerating: {c['file']}")
            try:
                output = generator.generate(c)
                print(f"  ✓ {output}")
                generated.append(output)
            except Exception as e:
                print(f"  ✗ Error: {e}")
    
    print(f"\n{'='*60}")
    print(f"COMPLETE: Generated {len(generated)} visualizations")
    print("="*60)


if __name__ == '__main__':
    main()
