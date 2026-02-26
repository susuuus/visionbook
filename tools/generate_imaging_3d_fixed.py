#!/usr/bin/env python3
"""
Proper 3D figure generation - analyze actual figures and use example templates
"""

from pathlib import Path
import shutil

# Map figures to their example templates
FIGURE_TEMPLATES = {
    "no_picture_on_a_wall_aina.png": {
        "name": "fig-wallpicture",
        "template_source": "/Users/su/Desktop/AI Augmented Book/Interactive Figures/pinhole.html",
        "description": "Pinhole camera with tree, apple, projection wall"
    },
    "brdf.png": {
        "name": "fig-lightSpray",  
        "template_source": "/Users/su/Downloads/light_surface_3d (10).html",
        "description": "BRDF light-surface interaction with incident/reflected rays"
    }
}

def copy_with_title_update(source_path: Path, dest_path: Path, new_title: str, fig_name: str):
    """Copy HTML and update title"""
    with open(source_path, 'r') as f:
        content = f.read()
    
    # Update title
    content = content.replace('<title>Fig 5.3 (b) Pinhole Camera</title>', 
                            f'<title>{new_title}</title>')
    content = content.replace('<title>Light-Surface Interaction</title>',
                            f'<title>{new_title}</title>')
    
    with open(dest_path, 'w') as f:
        f.write(content)
    
    print(f"✓ Copied and updated: {dest_path.name}")

def generate_camera_coordinates_html(output_path: Path):
    """Generate camera coordinates figure (pinhole_names2.png)"""
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>Camera Coordinate Systems</title>
<style>
    body { margin: 0; overflow: hidden; font-family: sans-serif; }
    .label {
      position: absolute;
      font-size: 16px;
      color: black;
      font-weight: bold;
      transform: translate(-50%, -50%);
      pointer-events: none;
      z-index: 1;
    }
</style>
</head>
<body>

<script type="module">
import * as THREE from 'https://esm.sh/three';
import { OrbitControls } from 'https://esm.sh/three/examples/jsm/controls/OrbitControls';

const scene = new THREE.Scene();
scene.background = new THREE.Color(0xffffff);

const aspect = window.innerWidth / window.innerHeight;
const d = 5;
const camera = new THREE.OrthographicCamera(-d * aspect, d * aspect, d, -d, 0.1, 100);
camera.position.set(4, 4, 4);
camera.lookAt(0, 0, 0);

const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;

// Pinhole at origin
const pinhole = new THREE.Mesh(
  new THREE.SphereGeometry(0.1, 16, 16),
  new THREE.MeshBasicMaterial({ color: 0x000000 })
);
scene.add(pinhole);

// Virtual camera plane at distance f=1
const f = 1.0;
const planeGeo = new THREE.PlaneGeometry(3, 2);
const planeMat = new THREE.MeshBasicMaterial({ 
  color: 0xe8f4f8, 
  side: THREE.DoubleSide, 
  transparent: true, 
  opacity: 0.6 
});
const virtualPlane = new THREE.Mesh(planeGeo, planeMat);
virtualPlane.rotation.y = -Math.PI / 2;
virtualPlane.position.set(f, 0, 0);
scene.add(virtualPlane);

const edges = new THREE.EdgesGeometry(planeGeo);
const edgeLine = new THREE.LineSegments(edges, 
  new THREE.LineBasicMaterial({ color: 0x000000, linewidth: 2 }));
edgeLine.rotation.copy(virtualPlane.rotation);
edgeLine.position.copy(virtualPlane.position);
scene.add(edgeLine);

// World coordinate axes (X, Y, Z) - RED
const axisLength = 2.5;
const xAxisWorld = new THREE.ArrowHelper(
  new THREE.Vector3(1, 0, 0), new THREE.Vector3(0, 0, 0), 
  axisLength, 0xff0000, 0.2, 0.15
);
const yAxisWorld = new THREE.ArrowHelper(
  new THREE.Vector3(0, 1, 0), new THREE.Vector3(0, 0, 0), 
  axisLength, 0xff0000, 0.2, 0.15
);
const zAxisWorld = new THREE.ArrowHelper(
  new THREE.Vector3(0, 0, 1), new THREE.Vector3(0, 0, 0), 
  axisLength, 0xff0000, 0.2, 0.15
);
scene.add(xAxisWorld, yAxisWorld, zAxisWorld);

// Camera/Image plane axes (x, y) - GREEN
const imagePlaneOrigin = new THREE.Vector3(f, -1, 1.5);
const xAxisImage = new THREE.ArrowHelper(
  new THREE.Vector3(0, 1, 0), imagePlaneOrigin, 
  1, 0x00aa00, 0.15, 0.1
);
const yAxisImage = new THREE.ArrowHelper(
  new THREE.Vector3(0, 0, -1), imagePlaneOrigin, 
  1, 0x00aa00, 0.15, 0.1
);
scene.add(xAxisImage, yAxisImage);

// Labels
const labels = [];
const vector = new THREE.Vector3();

function createLabel(text, pos) {
  const div = document.createElement('div');
  div.className = 'label';
  div.innerHTML = text;
  document.body.appendChild(div);
  return { div, pos };
}

labels.push(createLabel('<b>X</b>', new THREE.Vector3(axisLength + 0.3, 0, 0)));
labels.push(createLabel('<b>Y</b>', new THREE.Vector3(0, axisLength + 0.3, 0)));
labels.push(createLabel('<b>Z</b>', new THREE.Vector3(0, 0, axisLength + 0.3)));
labels.push(createLabel('<b>x</b>', imagePlaneOrigin.clone().add(new THREE.Vector3(0, 1.3, 0))));
labels.push(createLabel('<b>y</b>', imagePlaneOrigin.clone().add(new THREE.Vector3(0, 0, -1.3))));
labels.push(createLabel('Virtual Camera Plane', new THREE.Vector3(f, 1.3, 0)));
labels.push(createLabel('f', new THREE.Vector3(f/2, -0.3, 0)));

// Dashed line showing focal length
const fLine = new THREE.BufferGeometry().setFromPoints([
  new THREE.Vector3(0, 0, 0),
  new THREE.Vector3(f, 0, 0)
]);
const fDashed = new THREE.Line(fLine,
  new THREE.LineDashedMaterial({ color: 0x888888, dashSize: 0.1, gapSize: 0.1 }));
fDashed.computeLineDistances();
scene.add(fDashed);

function updateLabels() {
  labels.forEach(({ div, pos }) => {
    vector.copy(pos).project(camera);
    const x = (vector.x * 0.5 + 0.5) * window.innerWidth;
    const y = (-vector.y * 0.5 + 0.5) * window.innerHeight;
    div.style.left = `${x}px`;
    div.style.top = `${y}px`;
  });
}

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
</script>
</body>
</html>"""
    
    with open(output_path, 'w') as f:
        f.write(html)
    print(f"✓ Generated: {output_path.name}")

def generate_similar_triangles_fixed(output_path: Path):
    """Generate FIXED similar triangles figure"""
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>Similar Triangles - Perspective Projection</title>
<style>
    body { margin: 0; overflow: hidden; font-family: sans-serif; }
    .label {
      position: absolute;
      font-size: 16px;
      color: black;
      font-weight: bold;
      transform: translate(-50%, -50%);
      pointer-events: none;
      z-index: 1;
    }
</style>
</head>
<body>

<script type="module">
import * as THREE from 'https://esm.sh/three';
import { OrbitControls } from 'https://esm.sh/three/examples/jsm/controls/OrbitControls';

const scene = new THREE.Scene();
scene.background = new THREE.Color(0xffffff);

const aspect = window.innerWidth / window.innerHeight;
const d = 4;
const camera = new THREE.OrthographicCamera(-d * aspect, d * aspect, d, -d, 0.1, 100);
camera.position.set(4, 3, 4);
camera.lookAt(1.5, 0.5, 0);

const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;

const f = 1.0;
const Z = 3.0;
const X = 1.5;
const Y = 0.75;

// Origin
const origin = new THREE.Mesh(
  new THREE.SphereGeometry(0.08, 16, 16),
  new THREE.MeshBasicMaterial({ color: 0x000000 })
);
scene.add(origin);

// Image plane
const planeGeo = new THREE.PlaneGeometry(2, 1.5);
const planeMat = new THREE.MeshBasicMaterial({ 
  color: 0xe0e0ff, 
  side: THREE.DoubleSide, 
  transparent: true, 
  opacity: 0.5 
});
const imagePlane = new THREE.Mesh(planeGeo, planeMat);
imagePlane.rotation.y = -Math.PI / 2;
imagePlane.position.set(f, 0.5, 0);
scene.add(imagePlane);

const edges = new THREE.EdgesGeometry(planeGeo);
const edgeLine = new THREE.LineSegments(edges, 
  new THREE.LineBasicMaterial({ color: 0x000000 }));
edgeLine.rotation.copy(imagePlane.rotation);
edgeLine.position.copy(imagePlane.position);
scene.add(edgeLine);

// Point P
const pointP = new THREE.Mesh(
  new THREE.SphereGeometry(0.1, 16, 16),
  new THREE.MeshBasicMaterial({ color: 0xff0000 })
);
pointP.position.set(Z, Y, X);
scene.add(pointP);

// Projected point p
const x = f * X / Z;
const y = f * Y / Z;
const pointp = new THREE.Mesh(
  new THREE.SphereGeometry(0.08, 16, 16),
  new THREE.MeshBasicMaterial({ color: 0x0000ff })
);
pointp.position.set(f, y, x);
scene.add(pointp);

// Ray from O to P (RED)
const rayOP = new THREE.BufferGeometry().setFromPoints([
  origin.position.clone(),
  pointP.position.clone()
]);
const rayOPline = new THREE.Line(rayOP, 
  new THREE.LineBasicMaterial({ color: 0xff0000, linewidth: 2 }));
scene.add(rayOPline);

// Small triangle vertical (GREEN dashed)
const smallTriBase = new THREE.BufferGeometry().setFromPoints([
  new THREE.Vector3(f, 0, 0),
  new THREE.Vector3(f, y, 0)
]);
const smallTriBaseLine = new THREE.Line(smallTriBase,
  new THREE.LineDashedMaterial({ color: 0x00aa00, dashSize: 0.05, gapSize: 0.05 }));
smallTriBaseLine.computeLineDistances();
scene.add(smallTriBaseLine);

// Large triangle vertical (GREEN dashed)
const largeTriBase = new THREE.BufferGeometry().setFromPoints([
  new THREE.Vector3(Z, 0, 0),
  new THREE.Vector3(Z, Y, 0)
]);
const largeTriBaseLine = new THREE.Line(largeTriBase,
  new THREE.LineDashedMaterial({ color: 0x00aa00, dashSize: 0.05, gapSize: 0.05 }));
largeTriBaseLine.computeLineDistances();
scene.add(largeTriBaseLine);

// Base lines (GREEN solid)
const smallBase = new THREE.BufferGeometry().setFromPoints([
  origin.position.clone(),
  new THREE.Vector3(f, 0, 0)
]);
const smallBaseLine = new THREE.Line(smallBase,
  new THREE.LineBasicMaterial({ color: 0x00aa00, linewidth: 2 }));
scene.add(smallBaseLine);

const largeBase = new THREE.BufferGeometry().setFromPoints([
  origin.position.clone(),
  new THREE.Vector3(Z, 0, 0)
]);
const largeBaseLine = new THREE.Line(largeBase,
  new THREE.LineBasicMaterial({ color: 0x00aa00, linewidth: 2 }));
scene.add(largeBaseLine);

// Z axis
const zAxis = new THREE.ArrowHelper(
  new THREE.Vector3(1, 0, 0), origin.position, 4, 0x888888, 0.2, 0.1
);
scene.add(zAxis);

// Labels
const labels = [];
const vector = new THREE.Vector3();

function createLabel(text, pos) {
  const div = document.createElement('div');
  div.className = 'label';
  div.innerHTML = text;
  document.body.appendChild(div);
  return { div, pos };
}

labels.push(createLabel('O', new THREE.Vector3(-0.2, -0.1, 0)));
labels.push(createLabel('P(X,Y,Z)', pointP.position.clone().add(new THREE.Vector3(0.3, 0.2, 0))));
labels.push(createLabel('p(x,y)', pointp.position.clone().add(new THREE.Vector3(0, 0.2, 0))));
labels.push(createLabel('f', new THREE.Vector3(f/2, -0.2, 0)));
labels.push(createLabel('Z', new THREE.Vector3(Z/2, -0.2, 0)));
labels.push(createLabel('Y', new THREE.Vector3(Z+0.2, Y/2, 0)));
labels.push(createLabel('y', new THREE.Vector3(f+0.2, y/2, 0)));

function updateLabels() {
  labels.forEach(({ div, pos }) => {
    vector.copy(pos).project(camera);
    const x = (vector.x * 0.5 + 0.5) * window.innerWidth;
    const y = (-vector.y * 0.5 + 0.5) * window.innerHeight;
    div.style.left = `${x}px`;
    div.style.top = `${y}px`;
  });
}

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
</script>
</body>
</html>"""
    
    with open(output_path, 'w') as f:
        f.write(html)
    print(f"✓ Fixed and generated: {output_path.name}")

def main():
    output_dir = Path("interactive_figures/imaging")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("="*60)
    print("PROPER 3D Figure Generation - Using Example Templates")
    print("="*60)
    print()
    
    # 1. Copy pinhole camera example (for wallpicture figure)
    pinhole_source = Path("/Users/su/Desktop/AI Augmented Book/Interactive Figures/pinhole.html")
    if pinhole_source.exists():
        copy_with_title_update(
            pinhole_source,
            output_dir / "fig-wallpicture_3d.html",
            "Pinhole Camera - Wall Picture",
            "fig-wallpicture"
        )
    
    # 2. Copy BRDF example (for light-surface figure)  
    brdf_source = Path("/Users/su/Downloads/light_surface_3d (10).html")
    if brdf_source.exists():
        copy_with_title_update(
            brdf_source,
            output_dir / "fig-lightSpray_3d.html",
            "Light-Surface Interaction (BRDF)",
            "fig-lightSpray"
        )
    
    # 3. Generate camera coordinates (new)
    generate_camera_coordinates_html(output_dir / "fig-pinhole_names_3d.html")
    
    # 4. Fix similar triangles (was broken)
    generate_similar_triangles_fixed(output_dir / "fig-pinholeGeometry2_3d.html")
    
    print()
    print("="*60)
    print("✓ All figures generated successfully!")
    print("="*60)
    print()
    print("Generated files:")
    for f in sorted(output_dir.glob("*.html")):
        print(f"  - {f.name}")

if __name__ == '__main__':
    main()
