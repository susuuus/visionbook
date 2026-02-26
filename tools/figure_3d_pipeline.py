#!/usr/bin/env python3
"""
Automated 3D Figure Generation Pipeline for Vision Book
Processes chapter figures and generates 3D interactive visualizations
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from PIL import Image
import numpy as np

class Figure3DPipeline:
    """Pipeline to classify and convert 2D figures to 3D visualizations"""
    
    def __init__(self, chapter_path: str, figures_dir: str):
        self.chapter_path = Path(chapter_path)
        self.figures_dir = Path(figures_dir)
        self.output_dir = Path("interactive_figures")
        self.output_dir.mkdir(exist_ok=True)
        
        # Known 3D figure patterns based on examples
        self.existing_3d = {
            "homographies.html": "homography projection",
            "pinhole.html": "pinhole camera geometry", 
            "combined.html": "neural network transformations",
            "light_surface_3d.html": "light-surface interaction"
        }
    
    def extract_figure_references(self) -> List[Dict]:
        """Extract all figure references from the chapter QMD file"""
        with open(self.chapter_path, 'r') as f:
            content = f.read()
        
        # Find all figure references
        figures = []
        
        # Pattern 1: ![caption](path){#fig-id ...}
        pattern1 = r'!\[(.*?)\]\((figures/[^)]+?)\)\{#(fig-[\w-]+)[^}]*\}'
        matches1 = re.findall(pattern1, content)
        
        for caption, path, fig_id in matches1:
            figures.append({
                'caption': caption,
                'path': path,
                'id': fig_id,
                'full_path': self.chapter_path.parent / path
            })
        
        # Pattern 2: figures referenced in @fig-id format (find the actual figure definition)
        # This catches complex multi-panel figures
        pattern2 = r'!\[(.*?)\]\((figures/[^)]+?)\)\{[^}]*#(fig-[\w-]+)[^}]*\}'
        matches2 = re.findall(pattern2, content)
        
        # Deduplicate based on fig_id
        existing_ids = {fig['id'] for fig in figures}
        for caption, path, fig_id in matches2:
            if fig_id not in existing_ids:
                figures.append({
                    'caption': caption,
                    'path': path,
                    'id': fig_id,
                    'full_path': self.chapter_path.parent / path
                })
                existing_ids.add(fig_id)
        
        return figures
    
    def classify_figure(self, fig_info: Dict) -> Dict:
        """
        Classify if figure is suitable for 3D conversion
        Returns: {suitable: bool, reason: str, figure_type: str, primitives: list}
        """
        img_path = fig_info['full_path']
        
        # Skip if file doesn't exist or is not an image
        if not img_path.exists():
            return {'suitable': False, 'reason': 'File not found', 'figure_type': 'unknown'}
        
        ext = img_path.suffix.lower()
        if ext not in ['.png', '.jpg', '.jpeg']:
            return {'suitable': False, 'reason': 'Not a raster image', 'figure_type': 'unknown'}
        
        # Load image
        try:
            img = Image.open(img_path)
            img_array = np.array(img)
        except Exception as e:
            return {'suitable': False, 'reason': f'Cannot load image: {e}', 'figure_type': 'unknown'}
        
        # Analyze image characteristics
        fig_id = fig_info['id']
        caption = fig_info['caption'].lower()
        
        # Rule-based classification
        
        # 1. Check if it's a photograph (high color variance, noise patterns)
        if self._is_photograph(img_array):
            return {'suitable': False, 'reason': 'Photograph', 'figure_type': 'photograph'}
        
        # 2. Check for geometric diagrams with perspective cues
        if self._has_perspective_geometry(fig_id, caption, img_array):
            primitives = self._extract_geometric_primitives(fig_id, caption, img_array)
            return {
                'suitable': True, 
                'reason': 'Geometric diagram with perspective',
                'figure_type': '3d_geometry',
                'primitives': primitives
            }
        
        # 3. Check for simple 2D diagrams (no perspective)
        if self._is_simple_diagram(img_array):
            return {'suitable': False, 'reason': 'Simple 2D diagram', 'figure_type': '2d_diagram'}
        
        return {'suitable': False, 'reason': 'Unclear classification', 'figure_type': 'unknown'}
    
    def _is_photograph(self, img_array: np.ndarray) -> bool:
        """Detect if image is a photograph vs diagram"""
        # Convert to grayscale if needed
        if len(img_array.shape) == 3:
            gray = np.mean(img_array, axis=2)
        else:
            gray = img_array
        
        # Photographs typically have:
        # - High local variance (noise, textures)
        # - Gradual color transitions
        # - Many unique colors
        
        # Calculate local variance
        from scipy.ndimage import generic_filter
        local_var = generic_filter(gray, np.var, size=5)
        avg_local_var = np.mean(local_var)
        
        # High local variance suggests photograph
        if avg_local_var > 500:  # Threshold tuned for typical images
            return True
        
        # Count unique colors
        if len(img_array.shape) == 3:
            # Flatten to count unique RGB combinations
            reshaped = img_array.reshape(-1, img_array.shape[2])
            unique_colors = len(np.unique(reshaped, axis=0))
            # Diagrams typically have < 50 distinct colors, photos have thousands
            if unique_colors > 1000:
                return True
        
        return False
    
    def _has_perspective_geometry(self, fig_id: str, caption: str, img_array: np.ndarray) -> bool:
        """Detect perspective cues indicating 3D-suitable geometry"""
        
        # Keywords that suggest 3D geometry
        perspective_keywords = [
            'pinhole', 'camera', 'projection', 'perspective', '3d', 'geometry',
            'coordinate', 'plane', 'axis', 'ray', 'surface', 'normal',
            'orthographic', 'similar triangles', 'world', 'virtual'
        ]
        
        # Check caption and figure ID for keywords
        text = (fig_id + ' ' + caption).lower()
        if any(kw in text for kw in perspective_keywords):
            # Additional check: diagrams typically have fewer colors and cleaner lines
            if len(img_array.shape) == 3:
                reshaped = img_array.reshape(-1, img_array.shape[2])
                unique_colors = len(np.unique(reshaped, axis=0))
                # Geometric diagrams have limited color palette
                if unique_colors < 500:
                    return True
        
        return False
    
    def _is_simple_diagram(self, img_array: np.ndarray) -> bool:
        """Detect simple 2D diagrams without 3D elements"""
        # Simple diagrams have low variance and few colors
        if len(img_array.shape) == 3:
            reshaped = img_array.reshape(-1, img_array.shape[2])
            unique_colors = len(np.unique(reshaped, axis=0))
            return unique_colors < 100
        return True
    
    def _extract_geometric_primitives(self, fig_id: str, caption: str, 
                                     img_array: np.ndarray) -> List[Dict]:
        """
        Extract geometric primitives from figure based on semantic understanding
        This uses figure ID and caption to infer 3D structure
        """
        primitives = []
        
        # Map specific figures to their geometric primitives
        # Based on analysis of the imaging chapter
        
        if 'pinhole' in fig_id or 'pinhole' in caption.lower():
            primitives = self._define_pinhole_primitives(fig_id, caption)
        elif 'perspective' in fig_id or 'projection' in caption.lower():
            primitives = self._define_projection_primitives(fig_id, caption)
        elif 'similar' in caption.lower() and 'triangle' in caption.lower():
            primitives = self._define_similar_triangles_primitives()
        elif 'orthographic' in caption.lower() or 'orthogonal' in caption.lower():
            primitives = self._define_orthographic_primitives()
        elif 'brdf' in fig_id or 'light' in caption.lower():
            primitives = self._define_brdf_primitives()
        elif 'camera' in caption.lower() and 'coordinate' in caption.lower():
            primitives = self._define_camera_coordinates_primitives()
        
        return primitives
    
    def _define_pinhole_primitives(self, fig_id: str, caption: str) -> List[Dict]:
        """Define primitives for pinhole camera figures"""
        # Check specific pinhole figure types
        if 'geometry' in fig_id or 'names' in fig_id:
            return [
                {'type': 'plane', 'name': 'projection_plane', 'position': [0, 0, 0], 
                 'rotation': [0, -90, 0], 'size': [3, 2], 'color': 0xffffff, 'opacity': 0.6},
                {'type': 'plane', 'name': 'pinhole_wall', 'position': [2, 0, 0],
                 'rotation': [0, -90, 0], 'size': [4, 3], 'color': 0x000000, 'opacity': 1.0,
                 'has_hole': True, 'hole_radius': 0.05},
                {'type': 'point', 'name': 'pinhole', 'position': [2, 0, 0], 
                 'color': 0x000000, 'size': 0.1},
                {'type': 'arrow', 'name': 'optical_axis', 'from': [2, 0, 0], 
                 'to': [0, 0, 0], 'color': 0x000000},
                {'type': 'label', 'text': 'Pinhole', 'position': [2, 1.7, 0]},
                {'type': 'label', 'text': 'Wall', 'position': [0, 1.7, 0]}
            ]
        elif 'wall' in caption.lower() or 'picture' in caption.lower():
            return [
                {'type': 'plane', 'name': 'wall', 'position': [0, 0, 0],
                 'rotation': [0, -90, 0], 'size': [4, 3], 'color': 0xffffff, 'opacity': 0.8},
                {'type': 'object', 'name': 'scene_object', 'position': [4, 0, 0],
                 'object_type': 'tree'},
                {'type': 'rays', 'name': 'scattered_rays', 'from_object': True,
                 'count': 20, 'color': 0xffff00, 'dashed': True}
            ]
        else:
            # Generic pinhole setup
            return [
                {'type': 'plane', 'name': 'sensor', 'position': [0, 0, 0]},
                {'type': 'point', 'name': 'pinhole', 'position': [1, 0, 0]},
                {'type': 'object', 'name': 'scene', 'position': [3, 0, 0]}
            ]
    
    def _define_projection_primitives(self, fig_id: str, caption: str) -> List[Dict]:
        """Define primitives for projection geometry figures"""
        return [
            {'type': 'plane', 'name': 'image_plane', 'position': [1, 0, 0],
             'rotation': [0, -90, 0], 'size': [3, 2], 'color': 0xffffff},
            {'type': 'point', 'name': 'camera_center', 'position': [0, 0, 0]},
            {'type': 'plane', 'name': 'world_plane', 'position': [3, -0.5, 0],
             'rotation': [-70, -60, 0], 'size': [2, 1.2], 'color': 0xff9933, 'opacity': 0.3},
            {'type': 'axes', 'name': 'world_axes', 'position': [3, -0.5, 0],
             'length': 0.5, 'color': 0xff0000},
            {'type': 'point', 'name': 'world_point', 'position': [3.3, -0.3, 0],
             'color': 0x0000ff, 'size': 0.05},
            {'type': 'projection', 'from': 'world_point', 'to': 'image_plane',
             'through': 'camera_center', 'color': 0x0000ff, 'dashed': True}
        ]
    
    def _define_similar_triangles_primitives(self) -> List[Dict]:
        """Define primitives for similar triangles figure"""
        return [
            {'type': 'point', 'name': 'origin', 'position': [0, 0, 0], 'label': 'O'},
            {'type': 'plane', 'name': 'image_plane', 'position': [1, 0, 0],
             'rotation': [0, -90, 0], 'size': [2, 1.5], 'color': 0xe0e0ff, 'opacity': 0.5},
            {'type': 'point', 'name': 'P', 'position': [3, 1.5, 0.5], 
             'color': 0xff0000, 'label': 'P(X,Y,Z)'},
            {'type': 'point', 'name': 'p', 'position': [1, 0.5, 0.167],
             'color': 0x0000ff, 'label': 'p(x,y)'},
            {'type': 'line', 'from': [0, 0, 0], 'to': [3, 1.5, 0.5],
             'color': 0xff0000, 'dashed': True},
            {'type': 'line', 'from': [0, 0, 0], 'to': [3, 0, 0],
             'color': 0x00ff00, 'style': 'axis'},
            {'type': 'line', 'from': [3, 0, 0], 'to': [3, 1.5, 0],
             'color': 0x00ff00, 'dashed': True},
            {'type': 'line', 'from': [1, 0, 0], 'to': [1, 0.5, 0],
             'color': 0x0000ff, 'dashed': True},
            {'type': 'label', 'text': 'f', 'position': [0.5, -0.2, 0]},
            {'type': 'label', 'text': 'Z', 'position': [1.5, -0.2, 0]}
        ]
    
    def _define_orthographic_primitives(self) -> List[Dict]:
        """Define primitives for orthographic projection figure"""
        return [
            {'type': 'plane', 'name': 'projection_plane', 'position': [0, 0, 0],
             'rotation': [0, -90, 0], 'size': [3, 3], 'color': 0xffffff, 'opacity': 0.5},
            {'type': 'object', 'name': 'scene_object', 'position': [2, 0, 0],
             'object_type': 'cube', 'size': 0.5},
            {'type': 'rays', 'name': 'parallel_rays', 'direction': [-1, 0, 0],
             'count': 9, 'spacing': 0.3, 'color': 0x00ff00, 'dashed': True,
             'start_x': 3},
            {'type': 'label', 'text': 'x = X', 'position': [-0.5, 1.5, 0]},
            {'type': 'label', 'text': 'y = Y', 'position': [-0.5, -1.5, 0]}
        ]
    
    def _define_brdf_primitives(self) -> List[Dict]:
        """Define primitives for BRDF/light interaction figure"""
        return [
            {'type': 'plane', 'name': 'surface', 'position': [0, 0, 0],
             'rotation': [-90, 0, 0], 'size': [6, 4], 'color': 0x76ff03, 'opacity': 0.7},
            {'type': 'arrow', 'name': 'incident_ray', 'from': [-2, 3, 1],
             'to': [0, 0, 0], 'color': 0xffeb3b, 'gradient': True},
            {'type': 'arrow', 'name': 'normal', 'from': [0, 0, 0],
             'to': [0, 1.2, 0], 'color': 0x000000, 'width': 3},
            {'type': 'arrows', 'name': 'reflected_rays', 'origin': [0, 0, 0],
             'count': 8, 'distribution': 'specular_diffuse', 'color': 0x4caf50},
            {'type': 'label', 'text': 'ℓ_in(λ)', 'position': [-1, 2.5, 0.5]},
            {'type': 'label', 'text': 'n', 'position': [0.3, 0.8, 0]},
            {'type': 'label', 'text': 'ℓ_out = F(ℓ_in, n, λ, p, q)', 
             'position': [2.5, 1.5, 0], 'scale': [3, 0.75]}
        ]
    
    def _define_camera_coordinates_primitives(self) -> List[Dict]:
        """Define primitives for camera coordinate system figure"""
        return [
            {'type': 'point', 'name': 'camera_center', 'position': [0, 0, 0],
             'color': 0x000000, 'size': 0.1},
            {'type': 'plane', 'name': 'virtual_plane', 'position': [1, 0, 0],
             'rotation': [0, -90, 0], 'size': [3, 2], 'color': 0xffffff, 'opacity': 0.5},
            {'type': 'axes', 'name': 'camera_axes', 'position': [0, 0, 0],
             'x_color': 0xff0000, 'y_color': 0x00ff00, 'z_color': 0x0000ff},
            {'type': 'axes', 'name': 'image_axes', 'position': [1, -1, 1.5],
             'x_color': 0x00aa00, 'y_color': 0x00aa00},
            {'type': 'label', 'text': 'X', 'position': [0.6, 0, 0]},
            {'type': 'label', 'text': 'Y', 'position': [0, 0.6, 0]},
            {'type': 'label', 'text': 'Z', 'position': [0, 0, 0.6]},
            {'type': 'label', 'text': 'x', 'position': [1, 0.6, 1.5]},
            {'type': 'label', 'text': 'y', 'position': [1, -1, 0.9]}
        ]
    
    def generate_3d_html(self, fig_info: Dict, classification: Dict) -> Optional[str]:
        """Generate Three.js HTML file for the figure"""
        primitives = classification.get('primitives', [])
        if not primitives:
            return None
        
        fig_id = fig_info['id']
        output_path = self.output_dir / f"{fig_id}_3d.html"
        
        # Generate HTML content based on primitives
        html_content = self._create_html_template(fig_info, primitives)
        
        with open(output_path, 'w') as f:
            f.write(html_content)
        
        return str(output_path)
    
    def _create_html_template(self, fig_info: Dict, primitives: List[Dict]) -> str:
        """Create Three.js HTML template from primitives"""
        caption = fig_info['caption']
        fig_id = fig_info['id']
        
        # Generate Three.js setup code
        js_code = self._generate_threejs_code(primitives)
        
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{caption}</title>
    <style>
        body {{
            margin: 0;
            overflow: hidden;
            font-family: sans-serif;
            background: #ffffff;
        }}
        .label {{
            position: absolute;
            font-family: sans-serif;
            font-size: 13px;
            color: black;
            transform: translate(-50%, -50%);
            pointer-events: none;
            z-index: 1;
        }}
    </style>
</head>
<body>
    <script type="module">
        import * as THREE from 'https://esm.sh/three';
        import {{ OrbitControls }} from 'https://esm.sh/three/examples/jsm/controls/OrbitControls';
        
        {js_code}
    </script>
</body>
</html>"""
        return html
    
    def _generate_threejs_code(self, primitives: List[Dict]) -> str:
        """Generate Three.js code from primitive definitions"""
        
        # Basic scene setup
        code = """
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0xffffff);
        
        const aspect = window.innerWidth / window.innerHeight;
        const d = 5;
        const camera = new THREE.OrthographicCamera(-d * aspect, d * aspect, d, -d, 0.1, 100);
        camera.position.set(5, 5, 5);
        camera.lookAt(0, 0, 0);
        
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);
        
        const controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        
        // Lighting
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
        scene.add(ambientLight);
        const pointLight = new THREE.PointLight(0xffffff, 0.5);
        pointLight.position.set(5, 10, 5);
        scene.add(pointLight);
        
        const labels = [];
        const vector = new THREE.Vector3();
        
        function createLabel(text, pos) {
            const div = document.createElement('div');
            div.className = 'label';
            div.textContent = text;
            document.body.appendChild(div);
            labels.push({ div, pos });
        }
        
        function updateLabels() {
            labels.forEach(({ div, pos }) => {
                vector.copy(pos).project(camera);
                const x = (vector.x * 0.5 + 0.5) * window.innerWidth;
                const y = (-vector.y * 0.5 + 0.5) * window.innerHeight;
                div.style.left = `$${x}px`;
                div.style.top = `$${y}px`;
            });
        }
        
"""
        
        # Generate code for each primitive
        for prim in primitives:
            code += self._generate_primitive_code(prim)
        
        # Animation loop
        code += """
        function animate() {
            requestAnimationFrame(animate);
            controls.update();
            updateLabels();
            renderer.render(scene, camera);
        }
        animate();
        
        window.addEventListener('resize', () => {
            const aspect = window.innerWidth / window.innerHeight;
            camera.left = -d * aspect;
            camera.right = d * aspect;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });
"""
        
        return code
    
    def _generate_primitive_code(self, prim: Dict) -> str:
        """Generate Three.js code for a single primitive"""
        ptype = prim['type']
        
        if ptype == 'plane':
            return self._gen_plane_code(prim)
        elif ptype == 'point':
            return self._gen_point_code(prim)
        elif ptype == 'arrow':
            return self._gen_arrow_code(prim)
        elif ptype == 'line':
            return self._gen_line_code(prim)
        elif ptype == 'label':
            return self._gen_label_code(prim)
        elif ptype == 'axes':
            return self._gen_axes_code(prim)
        elif ptype == 'rays':
            return self._gen_rays_code(prim)
        elif ptype == 'projection':
            return self._gen_projection_code(prim)
        elif ptype == 'object':
            return self._gen_object_code(prim)
        else:
            return f"// Unknown primitive type: {ptype}\n"
    
    def _gen_plane_code(self, prim: Dict) -> str:
        pos = prim.get('position', [0, 0, 0])
        rot = prim.get('rotation', [0, 0, 0])
        size = prim.get('size', [2, 2])
        color = prim.get('color', 0xffffff)
        opacity = prim.get('opacity', 1.0)
        has_hole = prim.get('has_hole', False)
        
        code = f"""
        // Plane: {prim.get('name', 'plane')}
        {{
            const planeGeo = new THREE.PlaneGeometry({size[0]}, {size[1]});
            const planeMat = new THREE.MeshStandardMaterial({{
                color: {hex(color)},
                side: THREE.DoubleSide,
                transparent: {str(opacity < 1).lower()},
                opacity: {opacity},
                roughness: 0.5
            }});
            const plane = new THREE.Mesh(planeGeo, planeMat);
            plane.position.set({pos[0]}, {pos[1]}, {pos[2]});
            plane.rotation.set({rot[0] * np.pi / 180}, {rot[1] * np.pi / 180}, {rot[2] * np.pi / 180});
            scene.add(plane);
            
            // Add edge outline
            const edges = new THREE.EdgesGeometry(planeGeo);
            const edgeMat = new THREE.LineBasicMaterial({{ color: 0x000000 }});
            const edgeLines = new THREE.LineSegments(edges, edgeMat);
            edgeLines.position.copy(plane.position);
            edgeLines.rotation.copy(plane.rotation);
            scene.add(edgeLines);
        }}
"""
        return code
    
    def _gen_point_code(self, prim: Dict) -> str:
        pos = prim.get('position', [0, 0, 0])
        color = prim.get('color', 0x000000)
        size = prim.get('size', 0.1)
        
        return f"""
        // Point: {prim.get('name', 'point')}
        {{
            const pointGeo = new THREE.SphereGeometry({size}, 16, 16);
            const pointMat = new THREE.MeshBasicMaterial({{ color: {hex(color)} }});
            const point = new THREE.Mesh(pointGeo, pointMat);
            point.position.set({pos[0]}, {pos[1]}, {pos[2]});
            scene.add(point);
        }}
"""
    
    def _gen_arrow_code(self, prim: Dict) -> str:
        from_pos = prim.get('from', [0, 0, 0])
        to_pos = prim.get('to', [1, 0, 0])
        color = prim.get('color', 0x000000)
        
        dir_x = to_pos[0] - from_pos[0]
        dir_y = to_pos[1] - from_pos[1]
        dir_z = to_pos[2] - from_pos[2]
        length = np.sqrt(dir_x**2 + dir_y**2 + dir_z**2)
        
        return f"""
        // Arrow: {prim.get('name', 'arrow')}
        {{
            const dir = new THREE.Vector3({dir_x}, {dir_y}, {dir_z}).normalize();
            const origin = new THREE.Vector3({from_pos[0]}, {from_pos[1]}, {from_pos[2]});
            const arrow = new THREE.ArrowHelper(dir, origin, {length}, {hex(color)}, 0.15, 0.075);
            scene.add(arrow);
        }}
"""
    
    def _gen_line_code(self, prim: Dict) -> str:
        from_pos = prim.get('from', [0, 0, 0])
        to_pos = prim.get('to', [1, 0, 0])
        color = prim.get('color', 0x000000)
        dashed = prim.get('dashed', False)
        
        mat_type = 'LineDashedMaterial' if dashed else 'LineBasicMaterial'
        extra_props = ', dashSize: 0.1, gapSize: 0.1' if dashed else ''
        
        code = f"""
        // Line: {prim.get('name', 'line')}
        {{
            const points = [
                new THREE.Vector3({from_pos[0]}, {from_pos[1]}, {from_pos[2]}),
                new THREE.Vector3({to_pos[0]}, {to_pos[1]}, {to_pos[2]})
            ];
            const lineGeo = new THREE.BufferGeometry().setFromPoints(points);
            const lineMat = new THREE.{mat_type}({{ color: {hex(color)}{extra_props} }});
            const line = new THREE.Line(lineGeo, lineMat);
"""
        if dashed:
            code += "            line.computeLineDistances();\n"
        code += "            scene.add(line);\n        }\n"
        
        return code
    
    def _gen_label_code(self, prim: Dict) -> str:
        text = prim.get('text', '')
        pos = prim.get('position', [0, 0, 0])
        
        return f"""
        createLabel('{text}', new THREE.Vector3({pos[0]}, {pos[1]}, {pos[2]}));
"""
    
    def _gen_axes_code(self, prim: Dict) -> str:
        pos = prim.get('position', [0, 0, 0])
        length = prim.get('length', 1.0)
        x_color = prim.get('x_color', 0xff0000)
        y_color = prim.get('y_color', 0x00ff00)
        z_color = prim.get('z_color', 0x0000ff)
        
        return f"""
        // Axes: {prim.get('name', 'axes')}
        {{
            const origin = new THREE.Vector3({pos[0]}, {pos[1]}, {pos[2]});
            const xAxis = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), origin, {length}, {hex(x_color)});
            const yAxis = new THREE.ArrowHelper(new THREE.Vector3(0, 1, 0), origin, {length}, {hex(y_color)});
            const zAxis = new THREE.ArrowHelper(new THREE.Vector3(0, 0, 1), origin, {length}, {hex(z_color)});
            scene.add(xAxis, yAxis, zAxis);
        }}
"""
    
    def _gen_rays_code(self, prim: Dict) -> str:
        # Placeholder for ray generation
        return f"// Rays: {prim.get('name', 'rays')} (to be implemented)\n"
    
    def _gen_projection_code(self, prim: Dict) -> str:
        # Placeholder for projection lines
        return f"// Projection: {prim.get('name', 'projection')} (to be implemented)\n"
    
    def _gen_object_code(self, prim: Dict) -> str:
        # Placeholder for 3D objects
        return f"// Object: {prim.get('name', 'object')} (to be implemented)\n"
    
    def process_chapter(self) -> Dict:
        """Main processing pipeline"""
        print(f"\n{'='*60}")
        print(f"Processing chapter: {self.chapter_path.name}")
        print(f"{'='*60}\n")
        
        # Extract figures
        figures = self.extract_figure_references()
        print(f"Found {len(figures)} figures in chapter\n")
        
        results = {
            'total': len(figures),
            'suitable': 0,
            'processed': 0,
            'skipped': 0,
            'figures': []
        }
        
        # Process each figure
        for i, fig_info in enumerate(figures, 1):
            print(f"[{i}/{len(figures)}] Processing {fig_info['id']}...")
            print(f"  Caption: {fig_info['caption'][:60]}...")
            
            # Classify figure
            classification = self.classify_figure(fig_info)
            
            fig_result = {
                'id': fig_info['id'],
                'path': str(fig_info['path']),
                'caption': fig_info['caption'],
                'classification': classification
            }
            
            if classification['suitable']:
                print(f"  ✓ SUITABLE for 3D conversion")
                print(f"    Reason: {classification['reason']}")
                print(f"    Primitives: {len(classification.get('primitives', []))}")
                
                results['suitable'] += 1
                
                # Generate 3D HTML
                output_file = self.generate_3d_html(fig_info, classification)
                if output_file:
                    print(f"    Generated: {output_file}")
                    fig_result['output'] = output_file
                    results['processed'] += 1
                else:
                    print(f"    ✗ Generation failed")
            else:
                print(f"  ✗ Skipped: {classification['reason']}")
                results['skipped'] += 1
            
            results['figures'].append(fig_result)
            print()
        
        # Summary
        print(f"\n{'='*60}")
        print(f"SUMMARY")
        print(f"{'='*60}")
        print(f"Total figures: {results['total']}")
        print(f"Suitable for 3D: {results['suitable']}")
        print(f"Successfully processed: {results['processed']}")
        print(f"Skipped: {results['skipped']}")
        
        # Save results
        results_path = self.output_dir / 'processing_results.json'
        with open(results_path, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\nResults saved to: {results_path}")
        
        return results


def main():
    """Main entry point"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python figure_3d_pipeline.py <chapter.qmd>")
        print("Example: python figure_3d_pipeline.py imaging.qmd")
        sys.exit(1)
    
    chapter_file = sys.argv[1]
    chapter_path = Path(chapter_file)
    
    if not chapter_path.exists():
        print(f"Error: Chapter file not found: {chapter_path}")
        sys.exit(1)
    
    # Determine figures directory
    figures_dir = chapter_path.parent / 'figures' / chapter_path.stem
    
    if not figures_dir.exists():
        print(f"Error: Figures directory not found: {figures_dir}")
        sys.exit(1)
    
    # Run pipeline
    pipeline = Figure3DPipeline(str(chapter_path), str(figures_dir))
    results = pipeline.process_chapter()
    
    print(f"\n✓ Pipeline complete!")


if __name__ == '__main__':
    main()
