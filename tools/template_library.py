#!/usr/bin/env python3
"""
Template library for common 3D figure types
Reusable across chapters
"""

from pathlib import Path
from typing import Dict

def get_template_by_type(template_type: str, params: Dict) -> str:
    """Get HTML template with parameters filled in"""
    
    templates = {
        'projection_with_slider': _projection_slider_template,
        'ray_tracing': _ray_tracing_template,
        'coordinate_system': _coordinate_system_template,
        'parallel_rays': _parallel_rays_template,
    }
    
    if template_type in templates:
        return templates[template_type](params)
    else:
        raise ValueError(f"Unknown template type: {template_type}")

def _projection_slider_template(params: Dict) -> str:
    """Template for projection with adjustable parameters"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>{params['title']}</title>
<style>
    body {{ margin: 0; overflow: hidden; font-family: sans-serif; }}
    .label {{ position: absolute; font-size: 13px; color: black; 
              transform: translate(-50%, -50%); pointer-events: none; z-index: 1; }}
    .controls {{ position: absolute; top: 10px; left: 10px; 
                 background: #eee; padding: 10px; z-index: 10; }}
</style>
</head>
<body>
<div class="controls">
{params.get('controls_html', '')}
</div>

<script type="module">
import * as THREE from 'https://esm.sh/three';
import {{ OrbitControls }} from 'https://esm.sh/three/examples/jsm/controls/OrbitControls';

// Scene setup
const scene = new THREE.Scene();
scene.background = new THREE.Color(0xffffff);

const aspect = window.innerWidth / window.innerHeight;
const d = 5;
const camera = new THREE.OrthographicCamera(-d * aspect, d * aspect, d, -d, 0.1, 100);
camera.position.set({params.get('camera_x', 5)}, {params.get('camera_y', 5)}, {params.get('camera_z', 5)});
camera.lookAt(0, 0, 0);

const renderer = new THREE.WebGLRenderer({{ antialias: true }});
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;

// Add your 3D objects here
{params.get('scene_code', '')}

function animate() {{
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
}}
animate();

window.addEventListener('resize', () => {{
    const aspect = window.innerWidth / window.innerHeight;
    camera.left = -d * aspect;
    camera.right = d * aspect;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}});
</script>
</body>
</html>"""

def _ray_tracing_template(params: Dict) -> str:
    """Template for ray tracing visualizations"""
    # Similar structure...
    pass

def _coordinate_system_template(params: Dict) -> str:
    """Template for coordinate system figures"""
    # Similar structure...
    pass

def _parallel_rays_template(params: Dict) -> str:
    """Template for parallel ray diagrams"""
    # Similar structure...
    pass

# Registry of proven working templates
PROVEN_TEMPLATES = {
    'brdf_light_surface': '/Users/su/Downloads/light_surface_3d (10).html',
    'pinhole_camera': '/Users/su/Desktop/AI Augmented Book/Interactive Figures/pinhole.html',
    'homography': '/Users/su/Desktop/AI Augmented Book/Interactive Figures/homographies.html',
}

def copy_proven_template(template_name: str, output_path: Path, title: str = None):
    """Copy a proven working template"""
    import shutil
    
    if template_name not in PROVEN_TEMPLATES:
        raise ValueError(f"Template not found: {template_name}")
    
    source = Path(PROVEN_TEMPLATES[template_name])
    if not source.exists():
        raise FileNotFoundError(f"Source template missing: {source}")
    
    # Copy and optionally update title
    with open(source, 'r') as f:
        content = f.read()
    
    if title:
        # Update title tags
        content = content.replace('<title>Fig 5.3 (b) Pinhole Camera</title>', 
                                f'<title>{title}</title>')
        content = content.replace('<title>Light-Surface Interaction</title>',
                                f'<title>{title}</title>')
    
    with open(output_path, 'w') as f:
        f.write(content)
    
    return output_path
