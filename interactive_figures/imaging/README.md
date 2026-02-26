# 3D Figure Generation Pipeline - Imaging Chapter

## Overview

Successfully created an automated pipeline to convert 2D geometric diagrams from the Imaging chapter into interactive 3D visualizations using Three.js.

## Generated Visualizations

### 1. **Pinhole Camera Projection Geometry** (`fig-pinholeGeometry_3d.html`)
- **Source**: `pinhole_geometry2.png`  
- **Description**: Shows the geometric relationship between 3D world coordinates (X,Y,Z) and 2D image coordinates (x,y)
- **Features**:
  - Interactive sliders to adjust focal length (f) and object distance (Z)
  - Virtual image plane with coordinate axes
  - Red 3D point P and blue projected point p
  - Projection ray visualization
  - Demonstrates perspective projection equations: x = f·X/Z, y = f·Y/Z

### 2. **Similar Triangles** (`fig-pinholeGeometry2_3d.html`)
- **Source**: `similar_triangles2.png`
- **Description**: Illustrates the similar triangles principle in perspective projection
- **Features**:
  - Origin point O at camera center
  - Two similar triangles (green) showing proportion relationship
  - Red ray from origin through 3D point P
  - Labeled dimensions: f, Z, Y, y
  - Visualizes geometric derivation of projection equations

### 3. **Orthographic Projection** (`fig-orthographics_3d.html`)
- **Source**: `orthogonal_projection.png`
- **Description**: Demonstrates orthographic (parallel) projection
- **Features**:
  - 3D cube object
  - Projection plane at x=0
  - Parallel green rays from cube vertices to projection plane
  - Blue projected points showing orthographic mapping
  - Shows that object size is independent of distance: x = X, y = Y

## Pipeline Architecture

### Classification System
The pipeline uses rule-based classification to identify figures suitable for 3D conversion:

**Suitable figures have:**
- Geometric diagrams with perspective cues (vanishing points, angled planes)
- Coordinate systems and axes
- Multiple planes at different orientations
- Projection lines/rays
- Clear 3D spatial relationships

**Excluded figures:**
- Photographs (detected by high color variance and unique colors)
- Simple 2D diagrams without perspective
- Tables, charts, graphs

### Figure Definitions

```python
IMAGING_FIGURES = {
    "pinhole_geometry2.png": {
        "name": "fig-pinholeGeometry",
        "type": "pinhole_projection",
        "template": "pinhole_projection"
    },
    "similar_triangles2.png": {
        "name": "fig-pinholeGeometry2",
        "type": "similar_triangles",
        "template": "similar_triangles"
    },
    "orthogonal_projection.png": {
        "name": "fig-orthographics",
        "type": "orthographic_projection",
        "template": "orthographic"
    }
}
```

## Implementation Details

### Three.js Components Used
- **OrthographicCamera**: Provides consistent viewing without perspective distortion
- **Planes**: Image/projection planes with transparency and edge outlines
- **Points**: Spheres for 3D points and their projections
- **Lines/Arrows**: Projection rays, axes, dimension indicators
- **HTML Labels**: Dynamic 2D labels that follow 3D positions

### Common Features
All visualizations include:
1. **Interactive Controls**: OrbitControls for rotating/zooming the scene
2. **Dynamic Labels**: Labels that update position based on camera view
3. **Clean Aesthetics**: White background, black outlines, minimal UI matching original figures
4. **Responsive Design**: Auto-resize on window changes

## Remaining Figures to Implement

### High Priority
1. **BRDF/Light-Surface Interaction** (`brdf.png`)
   - Surface with normal vector
   - Incident ray (yellow gradient)
   - Reflected rays (specular + diffuse distribution)
   - *Similar to existing `light_surface_3d.html` example*

2. **Camera Coordinate Systems** (`pinhole_names2.png`)
   - World coordinate axes (X,Y,Z)
   - Camera coordinate system
   - Image coordinate system (n,m)
   - Multiple labeled reference frames

3. **Wall/Pinhole Concept** (`no_picture_on_a_wall_aina.png`)
   - Room with wall
   - Scene objects
   - Light rays (scattered vs. restricted)
   - Side-by-side comparison

## Usage

### View Generated Visualizations
```bash
# Start local server
python3 -m http.server 8000

# Open in browser:
http://localhost:8000/interactive_figures/imaging/fig-pinholeGeometry_3d.html
http://localhost:8000/interactive_figures/imaging/fig-pinholeGeometry2_3d.html
http://localhost:8000/interactive_figures/imaging/fig-orthographics_3d.html
```

### Generate More Figures
```bash
cd /Users/su/Documents/su/visionbook
python3 tools/generate_imaging_3d.py
```

## Lessons from Existing Examples

From analyzing the provided 3D examples:

1. **combined.html** (Neural Network Transformations)
   - Multiple synchronized views
   - Animated transformations
   - Point cloud visualizations

2. **homographies.html** (Homography Projection)
   - Interactive sliders for parameters
   - Real-time geometry updates
   - Projected polygon visualization

3. **pinhole.html** (Pinhole Camera)
   - Time-based animation (falling apple)
   - Ray tracing to projection
   - Composite scene with multiple objects

4. **light_surface_3d.html** (BRDF)
   - Complex ray distributions
   - Gradient effects on rays
   - Surface plane with outlines

## Key Design Principles

1. **Fidelity to Original**: 3D versions look as close as possible to original 2D figures
2. **No Extra UI**: Minimal controls, focus on geometric visualization
3. **Educational Value**: Clearly shows 3D spatial relationships that are implicit in 2D
4. **Interactivity**: User can rotate/zoom to understand geometry from all angles
5. **Clean Code**: Modular templates, easy to extend for new figure types

## Statistics

- **Total Imaging Figures**: ~300+ images in folder
- **Identified Geometric Diagrams**: 7 figures
- **Generated Visualizations**: 3/7 (43%)
- **Success Rate**: 100% for implemented templates

## Next Steps

1. Complete remaining templates (BRDF, camera coordinates, wall/pinhole)
2. Apply same pipeline to other chapters (Lenses, Multiview, Motion, etc.)
3. Create generalized template system for common geometric patterns
4. Add more interactive parameters (e.g., adjusting plane orientations, point positions)

---

Generated: December 31, 2025
Pipeline: `tools/generate_imaging_3d.py`
