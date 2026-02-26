#!/usr/bin/env python3
"""
Organize and classify figures into sorted folders
Then convert 3D candidates to interactive versions
"""

import shutil
from pathlib import Path
from PIL import Image
import numpy as np
import json
import re
from collections import defaultdict
import sys

class FigureOrganizer:
    """Classify and organize figures into folders"""
    
    def __init__(self, chapter_name: str, use_llm_verification: bool = False):
        self.chapter = chapter_name
        self.source_dir = Path(f"figures/{chapter_name}")
        self.base_output = Path(f"figures_sorted/{chapter_name}")
        self.qmd_file = Path(f"{chapter_name}.qmd")
        self.use_llm_verification = use_llm_verification
        self.qmd_context = {}  # Will store figure context from .qmd
        
        # Create organized folder structure
        self.folders = {
            'photographs': self.base_output / 'photographs',
            'diagrams_2d': self.base_output / 'diagrams_2d',
            'diagrams_3d_candidates': self.base_output / 'diagrams_3d_candidates',
            'interactive': Path(f"interactive_figures/{chapter_name}")
        }
        
        for folder in self.folders.values():
            folder.mkdir(parents=True, exist_ok=True)
    
    def extract_figures_from_qmd(self):
        """Extract figure references from the .qmd file"""
        if not self.qmd_file.exists():
            print(f"⚠️  Warning: {self.qmd_file} not found. Processing all figures.")
            return None
        
        with open(self.qmd_file, 'r') as f:
            content = f.read()
        
        # Find all figure references with context
        pattern = rf'!\[([^\]]*)\]\(figures/{self.chapter}/([a-zA-Z0-9_.-]+\.(?:png|jpg|JPG))\)([^\n]*)'
        matches = re.findall(pattern, content)
        
        used_figures = set()
        for caption, filename, metadata in matches:
            used_figures.add(filename)
            # Store context for each figure
            self.qmd_context[filename] = {
                'caption': caption.strip(),
                'metadata': metadata.strip()
            }
        
        # Also extract surrounding text context (paragraph before the figure)
        for filename in used_figures:
            pattern = rf'([^\n]*)\n[^\n]*figures/{self.chapter}/{re.escape(filename)}'
            context_match = re.search(pattern, content)
            if context_match:
                self.qmd_context[filename]['surrounding_text'] = context_match.group(1).strip()[-200:]  # Last 200 chars
        
        # Also extract figure groupings from layout-ncol, layout-nrow contexts
        figure_groups = self._extract_figure_groups(content)
        
        return {
            'used_figures': used_figures,
            'figure_groups': figure_groups
        }
    
    def _extract_figure_groups(self, content):
        """Extract figures that appear together in layouts"""
        groups = []
        
        # Match layout blocks: :::{layout-ncol="N" #fig-id} ... :::
        layout_pattern = r':::\{layout-[^}]+#(fig-[^\}]+)\}(.*?):::'
        
        for match in re.finditer(layout_pattern, content, re.DOTALL):
            fig_id = match.group(1)
            block_content = match.group(2)
            
            # Extract all figures in this block
            fig_pattern = rf'figures/{self.chapter}/([a-zA-Z0-9_.-]+\.(?:png|jpg|JPG))'
            figs_in_block = re.findall(fig_pattern, block_content)
            
            if len(figs_in_block) > 1:
                groups.append({
                    'id': fig_id,
                    'figures': figs_in_block
                })
        
        return groups
    
    def _group_by_naming_convention(self, figure_list):
        """Group figures by naming patterns (e.g., telescope1, telescope2, ...)"""
        groups = defaultdict(list)
        
        for fig in figure_list:
            # Remove extension and trailing numbers
            base_name = re.sub(r'\d+\.(png|jpg|JPG)$', '', fig)
            groups[base_name].append(fig)
        
        # Only return groups with multiple figures
        return {k: v for k, v in groups.items() if len(v) > 1}
    
    def _llm_verify_classification(self, fig_path: Path, auto_classification: dict) -> dict:
        """Use LLM to verify and potentially override automatic classification"""
        
        filename = fig_path.name
        context = self.qmd_context.get(filename, {})
        
        # Prepare prompt for LLM
        prompt = f"""Analyze this figure classification:

FIGURE: {filename}
AUTOMATIC CLASSIFICATION: {auto_classification['category']}
REASON: {auto_classification.get('reason', 'N/A')}
CONFIDENCE: {auto_classification.get('confidence', 0):.0%}

CONTEXT FROM DOCUMENT:
Caption: {context.get('caption', 'N/A')}
Metadata: {context.get('metadata', 'N/A')}
Surrounding text: {context.get('surrounding_text', 'N/A')}

IMAGE PROPERTIES:
File exists: {fig_path.exists()}

CLASSIFICATION OPTIONS:
1. photograph - Real-world photographs (room photos, actual camera setups, moon images, etc.)
2. diagrams_2d - Simple 2D illustrations (no 3D geometry concepts)
3. diagrams_3d_candidates - Geometric diagrams showing 3D concepts like:
   - Camera projection geometry (pinhole, perspective, orthographic)
   - 3D coordinate systems and transformations
   - Light-surface interactions (BRDF, rays)
   - Multi-view geometry, depth relationships

TASK: Review the automatic classification. Consider:
- Does the caption/context suggest 3D geometric concepts?
- Is this a rendered/synthetic diagram or a real photograph?
- Would this benefit from interactive 3D visualization?

Respond in JSON format:
{{
  "correct": true/false,
  "reasoning": "brief explanation",
  "override_category": "category_name" (only if incorrect),
  "confidence": 0.0-1.0
}}
"""
        
        print(f"\n🤖 LLM Verification for: {filename}")
        print(f"   Auto: {auto_classification['category']}")
        
        # This is a placeholder - in actual implementation, you'd call an LLM API
        # For now, return a confirmation of the auto classification
        # User can implement actual LLM call here (OpenAI, Claude, etc.)
        
        return {
            "correct": True,
            "reasoning": "LLM verification not implemented - using auto classification",
            "override_category": None,
            "confidence": auto_classification.get('confidence', 0.8)
        }
    
    def classify_and_sort(self):
        """Classify all figures and copy to appropriate folders"""
        
        # Extract figures from .qmd file
        qmd_data = self.extract_figures_from_qmd()
        
        if qmd_data:
            used_figures = qmd_data['used_figures']
            figure_groups = qmd_data['figure_groups']
            naming_groups = self._group_by_naming_convention(list(used_figures))
            
            print(f"📄 Found {len(used_figures)} figures referenced in {self.qmd_file}")
            if figure_groups:
                print(f"🔗 Found {len(figure_groups)} figure layouts")
            if naming_groups:
                print(f"👨‍👩‍👧‍👦 Found {len(naming_groups)} figure families by naming")
        else:
            used_figures = None
            figure_groups = []
            naming_groups = {}
        
        results = {
            'photographs': [],
            'diagrams_2d': [],
            'diagrams_3d_candidates': [],
            'unknown': [],
            'groups': {
                'layout_groups': figure_groups,
                'naming_groups': naming_groups
            }
        }
        
        print(f"\n📁 Processing: {self.source_dir}")
        print(f"📊 Organizing into: {self.base_output}")
        print("="*70)
        
        # Get all PNG and JPG files (including .JPG uppercase)
        all_figs = list(self.source_dir.glob("*.png")) + \
                   list(self.source_dir.glob("*.jpg")) + \
                   list(self.source_dir.glob("*.JPG"))
        
        # Filter: only process figures used in .qmd, skip multi-panel variants
        if used_figures:
            filtered_figs = [f for f in all_figs 
                           if f.name in used_figures 
                           and not f.stem.endswith(('-0', '-1', '-2'))]
        else:
            filtered_figs = [f for f in all_figs 
                           if not f.stem.endswith(('-0', '-1', '-2'))]
        
        total = len(filtered_figs)
        print(f"Processing {total} figures...\n")
        
        # Check which figures are already converted to interactive
        interactive_files = list(self.folders['interactive'].glob("*.html"))
        interactive_names = {f.stem for f in interactive_files if not f.name == 'index.html'}
        
        # Manual mapping of source figures to interactive names
        conversion_map = {
            'brdf': 'fig-lightSpray_3d',
            'orthogonal_projection': 'fig-orthographics_3d',
            'similar_triangles2': 'fig-pinholeGeometry2_3d',
            'pinhole_geometry2': 'fig-pinholeGeometry2_3d',
            'pinhole_names': 'fig-pinhole_names_3d',
            'pinhole_names2': 'fig-pinhole_names_3d',
            'pinhole_geometry': 'fig-pinholeGeometry_3d',
            'no_picture_on_a_wall': 'fig-wallpicture_3d',
        }
        
        for idx, fig_path in enumerate(sorted(filtered_figs), 1):
            classification = self._classify_figure(fig_path)
            
            # LLM verification if enabled
            if self.use_llm_verification:
                llm_result = self._llm_verify_classification(fig_path, classification)
                if not llm_result['correct'] and llm_result['override_category']:
                    print(f"   ⚠️  LLM Override: {classification['category']} → {llm_result['override_category']}")
                    print(f"   Reason: {llm_result['reasoning']}")
                    classification['category'] = llm_result['override_category']
                    classification['llm_verified'] = True
                    classification['llm_reasoning'] = llm_result['reasoning']
                else:
                    classification['llm_verified'] = True
                    classification['llm_reasoning'] = llm_result['reasoning']
            
            category = classification['category']
            
            # Check if already converted (check both direct match and mapping)
            fig_stem = fig_path.stem
            is_converted = (
                any(fig_stem in iname for iname in interactive_names) or
                conversion_map.get(fig_stem) in interactive_names
            )
            
            # Compact progress output
            if category in ['diagrams_3d_candidates']:
                status = "✅" if is_converted else "🎯"
                print(f"[{idx:3d}/{total}] {status} 3D: {fig_path.name}")
            elif idx % 10 == 0:  # Progress marker every 10 files
                print(f"[{idx:3d}/{total}] ...")
            
            # Copy to appropriate folder
            if category in ['photograph', 'diagrams_2d', 'diagrams_3d_candidates']:
                dest_folder = self.folders.get(
                    'photographs' if category == 'photograph' else 
                    'diagrams_2d' if category == 'diagrams_2d' else
                    'diagrams_3d_candidates'
                )
                dest_path = dest_folder / fig_path.name
                shutil.copy2(fig_path, dest_path)
                
                result_entry = {
                    'file': fig_path.name,
                    'classification': classification,
                    'converted': is_converted
                }
                
                results[category if category != 'photograph' else 'photographs'].append(result_entry)
            else:
                results['unknown'].append({
                    'file': fig_path.name,
                    'classification': classification
                })
        
        # Save classification results
        results_file = self.base_output / 'classification_results.json'
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        # Print summary
        print("\n" + "="*70)
        print("📊 CLASSIFICATION SUMMARY")
        print("="*70)
        print(f"Photographs: {len(results['photographs'])}")
        print(f"2D Diagrams: {len(results['diagrams_2d'])}")
        print(f"3D Candidates: {len(results['diagrams_3d_candidates'])}")
        print(f"Unknown: {len(results['unknown'])}")
        print(f"\n✓ Results saved: {results_file}")
        
        return results
    
    def _classify_figure(self, fig_path: Path) -> dict:
        """Classify a single figure"""
        try:
            img = Image.open(fig_path)
            img_array = np.array(img)
        except Exception as e:
            return {
                'category': 'unknown',
                'reason': f'Cannot load: {e}',
                'confidence': 0.0
            }
        
        filename = fig_path.stem.lower()
        
        # Check if 3D candidate FIRST (before photo check)
        candidate_result = self._is_3d_candidate(filename, img_array)
        if candidate_result['is_3d']:
            return {
                'category': 'diagrams_3d_candidates',
                'reason': candidate_result['reason'],
                'confidence': candidate_result['confidence'],
                'subcategory': candidate_result.get('subcategory', 'generic')
            }
        
        # Then check if photograph
        photo_result = self._is_photograph(filename, img_array)
        if photo_result['is_photo']:
            return {
                'category': 'photograph',
                'reason': photo_result['reason'],
                'confidence': photo_result['confidence']
            }
        
        # Check if 2D diagram
        if self._is_simple_diagram(img_array, filename):
            return {
                'category': 'diagrams_2d',
                'reason': 'Simple 2D diagram',
                'confidence': 0.8
            }
        
        return {
            'category': 'unknown',
            'reason': 'Could not classify',
            'confidence': 0.0
        }
    
    def _is_photograph(self, filename: str, img_array: np.ndarray) -> dict:
        """Check if image is a photograph vs colorful diagram"""
        
        # Filename-based photo detection
        photo_keywords = [
            'photo', 'moon', 'room', 'telescope', 
            'toby', 'gumby', 'jupiter', 'galileo', 'lunar',
            'laser', 'context', 'corner', 'snell', 'simple_pinhole'
        ]
        
        # Definite diagrams (even if colorful)
        diagram_keywords = [
            'brdf', 'pinhole_geometry', 'pinhole_names', 'pinhole_bag', 'projection', 'orthogonal',
            'perspective', 'coordinate', 'triangle', 'axis',
            'lens', 'ray', 'plane', 'amat', 'rendering', 'no_picture_on_a_wall', 'straw_camera'
        ]
        
        has_photo_keyword = any(kw in filename for kw in photo_keywords)
        has_diagram_keyword = any(kw in filename for kw in diagram_keywords)
        
        # Simple_pinhole is a photo despite having 'pinhole' in name
        if 'simple_pinhole' in filename:
            return {'is_photo': True, 'reason': 'Photo of pinhole demo', 'confidence': 0.95}
        
        # If clear diagram keyword, not a photo
        if has_diagram_keyword:
            return {'is_photo': False, 'reason': 'Diagram keyword', 'confidence': 0.9}
        
        # If clear photo keyword, it's a photo
        if has_photo_keyword:
            return {'is_photo': True, 'reason': 'Photo keyword in name', 'confidence': 0.95}
        
        # Image analysis for ambiguous cases
        if len(img_array.shape) < 2:
            return {'is_photo': False, 'reason': 'Invalid shape', 'confidence': 0}
        
        # File extension hint
        is_jpg = filename.endswith(('.jpg', '.jpeg'))
        
        gray = np.mean(img_array[:,:,:3], axis=2) if len(img_array.shape) == 3 else img_array
        
        # Calculate local variance (texture indicator)
        h, w = gray.shape
        local_vars = []
        patch_size = 10
        for i in range(0, min(h, 200), patch_size):
            for j in range(0, min(w, 200), patch_size):
                patch = gray[i:min(i+patch_size, h), j:min(j+patch_size, w)]
                if patch.size > 0:
                    local_vars.append(np.var(patch))
        
        avg_local_var = np.mean(local_vars) if local_vars else 0
        var_std = np.std(local_vars) if local_vars else 0
        
        # Count unique colors
        if len(img_array.shape) == 3:
            reshaped = img_array[:,:,:3].reshape(-1, 3)
            unique_colors = len(np.unique(reshaped, axis=0))
        else:
            unique_colors = len(np.unique(img_array))
        
        # Photos have: high variance, variable texture, many colors, often JPG
        # Diagrams have: moderate variance but uniform, fewer unique colors (even if colorful)
        photo_score = 0
        
        if avg_local_var > 600:
            photo_score += 2
        elif avg_local_var > 400:
            photo_score += 1
            
        if var_std > 300:  # Variable texture = photo
            photo_score += 2
            
        if unique_colors > 10000:  # Very many colors = photo
            photo_score += 2
        elif unique_colors > 2000:
            photo_score += 1
            
        if is_jpg:
            photo_score += 1
        
        is_photo = photo_score >= 3
        
        reason = f'Analysis: var={avg_local_var:.0f}, var_std={var_std:.0f}, colors={unique_colors}, score={photo_score}'
        
        return {
            'is_photo': is_photo,
            'reason': reason,
            'confidence': min(0.9, 0.6 + photo_score * 0.1)
        }
    
    def _is_3d_candidate(self, filename: str, img_array: np.ndarray) -> dict:
        """Check if diagram is suitable for 3D conversion"""
        
        # Strong 3D keywords
        strong_keywords = [
            'pinhole_geometry', 'pinhole_names', 'similar_triangle',
            'orthogonal_projection', 'orthographic', 'brdf',
            'corner_camera', 'no_picture', 'coordinate', 'perspective',
            'homography', 'projection', 'multiview', 'epipolar', 'straw_camera'
        ]
        
        # Weak 3D keywords
        weak_keywords = [
            'pinhole', 'camera', 'ray', 'lens', 'geometry',
            'axis', 'plane', 'depth', 'stereo'
        ]
        
        has_strong = any(kw in filename for kw in strong_keywords)
        has_weak = any(kw in filename for kw in weak_keywords)
        
        # Some figures are composite (include photos) but still show 3D concepts
        # Bypass color check for these
        composite_3d_figures = ['straw_camera', 'no_picture']
        is_composite = any(kw in filename for kw in composite_3d_figures)
        
        # Check if it's a diagram (limited colors) - unless it's a known composite
        if len(img_array.shape) == 3:
            reshaped = img_array[:,:,:3].reshape(-1, 3)
            unique_colors = len(np.unique(reshaped, axis=0))
            is_diagram = unique_colors < 2000 or is_composite
        else:
            is_diagram = True
        
        if has_strong and is_diagram:
            subcategory = self._identify_subcategory(filename)
            return {
                'is_3d': True,
                'reason': f'Strong 3D keywords + diagram characteristics',
                'confidence': 0.95,
                'subcategory': subcategory
            }
        elif has_weak and is_diagram:
            subcategory = self._identify_subcategory(filename)
            return {
                'is_3d': True,
                'reason': f'Weak 3D keywords + diagram characteristics',
                'confidence': 0.7,
                'subcategory': subcategory
            }
        
        return {'is_3d': False, 'reason': '', 'confidence': 0}
    
    def _identify_subcategory(self, filename: str) -> str:
        """Identify specific type of 3D diagram"""
        if 'brdf' in filename or 'light' in filename:
            return 'brdf_light_surface'
        elif 'similar' in filename and 'triangle' in filename:
            return 'similar_triangles'
        elif 'orthogonal' in filename or 'orthographic' in filename:
            return 'orthographic_projection'
        elif 'pinhole_geometry' in filename:
            return 'pinhole_projection'
        elif 'pinhole_names' in filename or 'coordinate' in filename:
            return 'camera_coordinates'
        elif 'no_picture' in filename or 'wall' in filename:
            return 'pinhole_scene'
        elif 'homography' in filename:
            return 'homography_projection'
        elif 'epipolar' in filename or 'multiview' in filename:
            return 'multiview_geometry'
        else:
            return 'generic_3d'
    
    def _is_simple_diagram(self, img_array: np.ndarray, filename: str = '') -> bool:
        """Check if it's a simple 2D diagram"""
        
        # Specific 2D diagram patterns (tutorial diagrams, rendering examples)
        # But exclude straw_camera which is a 3D concept
        if 'straw_camera' in filename.lower():
            return False
            
        simple_2d_keywords = ['bag', 'diffuse', 'phong', 'sphere']
        if any(kw in filename.lower() for kw in simple_2d_keywords):
            return True
        
        if len(img_array.shape) == 3:
            reshaped = img_array[:,:,:3].reshape(-1, 3)
            unique_colors = len(np.unique(reshaped, axis=0))
        else:
            unique_colors = len(np.unique(img_array))
        
        return unique_colors < 150


def main(chapter_name: str, use_llm: bool = False):
    """Main pipeline: organize and convert"""
    
    print("="*70)
    print("FIGURE ORGANIZATION AND 3D CONVERSION PIPELINE")
    if use_llm:
        print("🤖 LLM Verification: ENABLED")
    print("="*70)
    print()
    
    # Step 1: Organize figures
    organizer = FigureOrganizer(chapter_name, use_llm_verification=use_llm)
    results = organizer.classify_and_sort()
    
    # Step 2: Show 3D candidates
    candidates = results['diagrams_3d_candidates']
    
    if candidates:
        print("\n" + "="*70)
        print("🎯 3D CONVERSION CANDIDATES")
        print("="*70)
        
        converted_count = sum(1 for c in candidates if c.get('converted', False))
        remaining_count = len(candidates) - converted_count
        
        print(f"\n✅ Already converted: {converted_count}")
        print(f"🔲 Remaining to convert: {remaining_count}")
        print(f"📊 Total candidates: {len(candidates)}\n")
        
        # Show already converted
        if converted_count > 0:
            print("✅ CONVERTED:")
            for candidate in candidates:
                if candidate.get('converted', False):
                    print(f"  • {candidate['file']} ({candidate['classification'].get('subcategory', 'unknown')})")
        
        # Show remaining
        if remaining_count > 0:
            print(f"\n🔲 TODO ({remaining_count} figures):")
            for candidate in candidates:
                if not candidate.get('converted', False):
                    subcategory = candidate['classification'].get('subcategory', 'unknown')
                    confidence = candidate['classification']['confidence']
                    print(f"  • {candidate['file']}")
                    print(f"    └─ Type: {subcategory} (confidence: {confidence:.0%})")
        
        # Show groups
        if results['groups']['layout_groups']:
            print("\n🔗 FIGURE LAYOUTS (multi-panel groups):")
            for group in results['groups']['layout_groups']:
                print(f"  • {group['id']}: {', '.join(group['figures'])}")
        
        if results['groups']['naming_groups']:
            print("\n👨‍👩‍👧‍👦 FIGURE FAMILIES (by naming):")
            for base_name, figs in results['groups']['naming_groups'].items():
                print(f"  • {base_name}*: {', '.join(figs)}")
        
        print(f"\n📂 Candidates stored in:")
        print(f"   {organizer.folders['diagrams_3d_candidates']}")
        
        if remaining_count > 0:
            print(f"\n💡 Next step: Convert remaining {remaining_count} candidates")
            print(f"   python tools/convert_3d_candidates.py {chapter_name}")
    else:
        print("\n⚠️  No 3D candidates found")
    
    print("\n" + "="*70)
    print("📁 ORGANIZED STRUCTURE")
    print("="*70)
    for name, folder in organizer.folders.items():
        count = len(list(folder.glob("*.*")))
        print(f"  {folder}")
        print(f"    → {count} files")
    print()


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python tools/organize_figures.py <chapter_name> [--llm]")
        print("\nExample: python tools/organize_figures.py imaging")
        print("         python tools/organize_figures.py imaging --llm")
        print("\nOptions:")
        print("  --llm    Enable LLM verification of classifications")
        sys.exit(1)
    
    chapter = sys.argv[1]
    use_llm = '--llm' in sys.argv
    main(chapter, use_llm)
