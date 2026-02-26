#!/usr/bin/env python3
"""
Sophisticated 3D Figure Converter with Educational Context

Multi-stage LLM reasoning:
1. Educational Context Extraction - What concept is being taught?
2. Geometric Analysis - What 3D structures are present?
3. Reconstruction Planning - How to model it accurately?
4. Code Generation - Generate Three.js with proper geometry
5. Interaction Design - How should users explore it?
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
import re
import base64
from PIL import Image
import io

# Load .env file if it exists
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


@dataclass
class EducationalContext:
    """Context about what's being taught"""
    concept: str  # Main concept (e.g., "perspective projection", "pinhole camera")
    learning_objective: str  # What should the user understand?
    related_equations: List[str]  # Mathematical relationships
    key_terms: List[str]  # Technical vocabulary
    prerequisites: List[str]  # What concepts come before this


@dataclass
class GeometricStructure:
    """3D geometric elements in the figure"""
    elements: List[Dict]  # List of 3D objects (planes, lines, points, cameras)
    coordinate_system: str  # "world", "camera", "image"
    transformations: List[Dict]  # Projections, rotations, etc.
    annotations: List[Dict]  # Labels, arrows, measurements


@dataclass
class ConversionPlan:
    """Detailed plan for 3D conversion"""
    approach: str  # "geometric_reconstruction", "parametric_model", "scene_recreation"
    scene_graph: Dict  # Hierarchical structure of 3D objects
    camera_strategy: Dict  # Initial view, interaction modes
    animation_plan: Optional[Dict]  # If showing transformations
    code_structure: Dict  # How to organize the Three.js code


class Sophisticated3DConverter:
    """Advanced 3D converter with LLM reasoning"""
    
    def __init__(self, chapter: str):
        self.chapter = chapter
        self.chapter_path = Path(f"{chapter}.qmd")
        self.figures_path = Path(f"figures/{chapter}")
        self.output_path = Path(f"interactive_figures/{chapter}")
        self.output_path.mkdir(parents=True, exist_ok=True)
        
        # Load chapter content for context
        self.chapter_content = self._load_chapter_content()
        
        # Initialize LLM client
        self._init_llm()
    
    def _init_llm(self):
        """Initialize LLM with vision capabilities"""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not set. This converter requires GPT-4V or Claude with vision.")
        
        try:
            import openai
            self.llm_client = openai.OpenAI(api_key=api_key)
            self.has_vision = True  # GPT-4V for image analysis
        except ImportError:
            raise ImportError("Install openai: pip install openai")
    
    def _load_chapter_content(self) -> str:
        """Load full chapter for context"""
        if self.chapter_path.exists():
            with open(self.chapter_path, 'r') as f:
                return f.read()
        return ""
    
    def convert_figure(self, figure_path: Path, figure_id: str) -> Dict:
        """
        Multi-stage conversion process
        Returns: {html_path, educational_context, conversion_plan, code_quality}
        """
        print(f"\n{'='*70}")
        print(f"🎨 SOPHISTICATED 3D CONVERSION: {figure_path.name}")
        print(f"{'='*70}")
        
        # Stage 1: Extract educational context
        print("\n📚 Stage 1: Educational Context Analysis")
        edu_context = self._extract_educational_context(figure_path, figure_id)
        print(f"   Concept: {edu_context.concept}")
        print(f"   Objective: {edu_context.learning_objective[:80]}...")
        
        # Stage 2: Geometric analysis with vision
        print("\n🔍 Stage 2: Geometric Structure Analysis")
        geo_structure = self._analyze_geometry(figure_path, edu_context)
        print(f"   Elements: {len(geo_structure.elements)} objects")
        print(f"   Coordinate system: {geo_structure.coordinate_system}")
        
        # Stage 3: Conversion planning
        print("\n🗺️  Stage 3: Conversion Planning")
        conversion_plan = self._plan_conversion(edu_context, geo_structure)
        print(f"   Approach: {conversion_plan.approach}")
        print(f"   Scene graph: {len(conversion_plan.scene_graph.get('nodes', []))} nodes")
        
        # Stage 4: Code generation
        print("\n💻 Stage 4: Three.js Code Generation")
        html_code = self._generate_threejs_code(
            figure_id=figure_id,
            edu_context=edu_context,
            geo_structure=geo_structure,
            conversion_plan=conversion_plan
        )
        
        # Stage 5: Save and validate
        print("\n✅ Stage 5: Validation & Export")
        output_file = self.output_path / f"{figure_id}_3d.html"
        with open(output_file, 'w') as f:
            f.write(html_code)
        print(f"   Saved: {output_file}")
        
        return {
            'html_path': str(output_file),
            'educational_context': asdict(edu_context),
            'geometric_structure': {
                'elements': geo_structure.elements,
                'coordinate_system': geo_structure.coordinate_system
            },
            'conversion_plan': asdict(conversion_plan),
            'code_quality': self._validate_code(html_code)
        }
    
    def _extract_educational_context(self, figure_path: Path, figure_id: str) -> EducationalContext:
        """Use LLM to understand the pedagogical context"""
        
        # Find figure context in chapter
        figure_context = self._find_figure_context(figure_id)
        
        prompt = f"""Analyze this computer vision textbook figure and its educational context.

FIGURE ID: {figure_id}
FILENAME: {figure_path.name}

CHAPTER CONTEXT:
{figure_context['surrounding_text']}

CAPTION:
{figure_context['caption']}

TASK: Extract the educational intent of this figure.

Provide detailed JSON:
{{
  "concept": "The main 3D concept being taught (e.g., 'perspective projection', 'camera coordinate system')",
  "learning_objective": "What should students understand after seeing this figure?",
  "related_equations": ["List of mathematical equations/relationships shown or referenced"],
  "key_terms": ["Important technical terms students need to know"],
  "prerequisites": ["What concepts must be understood first?"]
}}

Focus on the PEDAGOGICAL purpose - what is this figure teaching about 3D geometry?"""
        
        try:
            response = self.llm_client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": self._get_education_system_prompt()},
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"},
                temperature=0.3
            )
            
            result = json.loads(response.choices[0].message.content)
            
            return EducationalContext(
                concept=result['concept'],
                learning_objective=result['learning_objective'],
                related_equations=result.get('related_equations', []),
                key_terms=result.get('key_terms', []),
                prerequisites=result.get('prerequisites', [])
            )
            
        except Exception as e:
            print(f"   ⚠️  Error extracting context: {e}")
            # Fallback
            return EducationalContext(
                concept="Unknown",
                learning_objective="Visualize 3D concept",
                related_equations=[],
                key_terms=[],
                prerequisites=[]
            )
    
    def _analyze_geometry(self, figure_path: Path, edu_context: EducationalContext) -> GeometricStructure:
        """Use vision LLM to analyze geometric structure"""
        
        # Encode image for vision model
        image_data = self._encode_image(figure_path)
        
        prompt = f"""Analyze this diagram's 3D geometric structure.

EDUCATIONAL CONTEXT: This figure teaches "{edu_context.concept}"

TASK: Identify all 3D geometric elements and their relationships.

For EACH element, specify:
1. Type (plane, line, point, camera, coordinate_system, ray, frustum, etc.)
2. Position/orientation in 3D space
3. Relationships to other elements (parallel, perpendicular, intersects, projects_to)
4. Visual properties (color, style, labels)

Provide detailed JSON:
{{
  "elements": [
    {{
      "id": "unique_id",
      "type": "plane|line|point|camera|frustum|coordinate_system|ray",
      "geometry": {{
        "position": [x, y, z],
        "orientation": [x, y, z] or "quaternion",
        "size": {{width, height, depth}} or "length"
      }},
      "relationships": [
        {{"to": "element_id", "type": "perpendicular|parallel|projects_to|contains"}}
      ],
      "visual": {{
        "color": "#hex",
        "label": "text if present",
        "style": "solid|dashed|arrow"
      }}
    }}
  ],
  "coordinate_system": "world|camera|image|screen",
  "transformations": [
    {{
      "type": "projection|rotation|translation",
      "from": "element_id",
      "to": "element_id",
      "matrix": "if applicable"
    }}
  ],
  "annotations": [
    {{
      "type": "label|arrow|dimension",
      "text": "annotation text",
      "position": [x, y, z],
      "points_to": "element_id"
    }}
  ]
}}

Be PRECISE about spatial relationships and transformations."""
        
        try:
            response = self.llm_client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are an expert in 3D computer graphics and geometric analysis."},
                    {"role": "user", "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_data}"}}
                    ]}
                ],
                response_format={"type": "json_object"},
                temperature=0.2,
                max_tokens=4000
            )
            
            result = json.loads(response.choices[0].message.content)
            
            return GeometricStructure(
                elements=result.get('elements', []),
                coordinate_system=result.get('coordinate_system', 'world'),
                transformations=result.get('transformations', []),
                annotations=result.get('annotations', [])
            )
            
        except Exception as e:
            print(f"   ⚠️  Error analyzing geometry: {e}")
            return GeometricStructure(elements=[], coordinate_system="world", transformations=[], annotations=[])
    
    def _plan_conversion(self, edu_context: EducationalContext, geo_structure: GeometricStructure) -> ConversionPlan:
        """Plan the conversion strategy"""
        
        prompt = f"""Create a detailed conversion plan for this 3D figure.

EDUCATIONAL CONTEXT:
- Concept: {edu_context.concept}
- Objective: {edu_context.learning_objective}

GEOMETRIC STRUCTURE:
- Elements: {len(geo_structure.elements)} objects
- Coordinate system: {geo_structure.coordinate_system}
- Transformations: {len(geo_structure.transformations)}

TASK: Design the interactive 3D scene.

Provide comprehensive JSON:
{{
  "approach": "geometric_reconstruction|parametric_model|scene_recreation",
  "scene_graph": {{
    "nodes": [
      {{
        "id": "node_id",
        "type": "group|mesh|line|camera_helper",
        "threejs_geometry": "BoxGeometry|PlaneGeometry|CylinderGeometry|BufferGeometry",
        "threejs_material": "MeshPhongMaterial|LineBasicMaterial|PointsMaterial",
        "parameters": {{}},
        "position": [x, y, z],
        "rotation": [x, y, z],
        "scale": [x, y, z],
        "children": ["child_ids"]
      }}
    ]
  }},
  "camera_strategy": {{
    "type": "OrthographicCamera|PerspectiveCamera",
    "initial_position": [x, y, z],
    "initial_look_at": [x, y, z],
    "controls": "OrbitControls|TrackballControls",
    "zoom_range": [min, max],
    "camera_animation": "optional camera path"
  }},
  "animation_plan": {{
    "enabled": true/false,
    "transformations": [
      {{
        "target": "element_id",
        "animation": "rotate|translate|morph",
        "duration": "seconds",
        "purpose": "show projection|demonstrate concept"
      }}
    ]
  }},
  "interaction_features": [
    "orbit_camera",
    "toggle_layers",
    "show_hide_elements",
    "step_through_transformation",
    "adjust_parameters"
  ],
  "educational_enhancements": [
    "show_axes",
    "label_elements",
    "highlight_relationships",
    "show_equations",
    "compare_views"
  ]
}}

Design for MAXIMUM educational clarity and accurate geometric relationships."""
        
        try:
            response = self.llm_client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are an expert in educational 3D visualization and Three.js."},
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"},
                temperature=0.4,
                max_tokens=3000
            )
            
            result = json.loads(response.choices[0].message.content)
            
            return ConversionPlan(
                approach=result.get('approach', 'geometric_reconstruction'),
                scene_graph=result.get('scene_graph', {}),
                camera_strategy=result.get('camera_strategy', {}),
                animation_plan=result.get('animation_plan'),
                code_structure=result.get('code_structure', {})
            )
            
        except Exception as e:
            print(f"   ⚠️  Error planning conversion: {e}")
            return ConversionPlan(approach="simple", scene_graph={}, camera_strategy={}, animation_plan=None, code_structure={})
    
    def _generate_threejs_code(self, figure_id: str, edu_context: EducationalContext, 
                                geo_structure: GeometricStructure, conversion_plan: ConversionPlan) -> str:
        """Generate sophisticated Three.js code"""
        
        # Build context for code generation
        context = {
            'figure_id': figure_id,
            'concept': edu_context.concept,
            'learning_objective': edu_context.learning_objective,
            'scene_graph': conversion_plan.scene_graph,
            'camera_strategy': conversion_plan.camera_strategy,
            'elements': geo_structure.elements,
            'annotations': geo_structure.annotations,
            'animation': conversion_plan.animation_plan
        }
        
        prompt = f"""Generate complete, production-ready Three.js code for this 3D educational figure.

CONTEXT:
{json.dumps(context, indent=2)}

REQUIREMENTS:
1. Implement ALL geometric elements from the scene graph
2. Use accurate 3D coordinates and transformations
3. Include educational annotations (labels, axes, helpers)
4. Implement camera strategy and controls
5. Add interactivity (if specified in animation_plan)
6. Use proper lighting for clarity
7. Include responsive canvas sizing
8. Add UI controls for educational features

Generate COMPLETE HTML with:
- Three.js r128 from CDN
- Full scene setup
- All geometries and materials
- Proper camera and controls
- Animation loop (if needed)
- Educational UI elements
- Responsive design

Make it EDUCATIONAL and ACCURATE to the original figure's geometry."""
        
        try:
            response = self.llm_client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": self._get_codegen_system_prompt()},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=4000
            )
            
            code = response.choices[0].message.content
            
            # Extract HTML if wrapped in code blocks
            if "```html" in code:
                code = code.split("```html")[1].split("```")[0].strip()
            elif "```" in code:
                code = code.split("```")[1].split("```")[0].strip()
            
            return code
            
        except Exception as e:
            print(f"   ⚠️  Error generating code: {e}")
            return self._fallback_template(figure_id, edu_context)
    
    def _encode_image(self, image_path: Path) -> str:
        """Encode image to base64 for vision API"""
        with Image.open(image_path) as img:
            # Resize if too large (vision APIs have limits)
            if img.width > 2000 or img.height > 2000:
                img.thumbnail((2000, 2000))
            
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            return base64.b64encode(buffer.getvalue()).decode()
    
    def _find_figure_context(self, figure_id: str) -> Dict:
        """Extract figure context from chapter"""
        pattern = rf'{figure_id}.*?\n(.*?)\n.*?!\[([^\]]*)\]'
        match = re.search(pattern, self.chapter_content, re.DOTALL)
        
        if match:
            return {
                'surrounding_text': match.group(1)[:500],
                'caption': match.group(2)
            }
        return {'surrounding_text': '', 'caption': ''}
    
    def _get_education_system_prompt(self) -> str:
        return """You are an expert in computer vision education and pedagogical design.

Your expertise:
- Understanding how 3D concepts are taught in vision courses
- Identifying key learning objectives from figures
- Extracting mathematical relationships from visual representations
- Recognizing prerequisite concepts

Focus on what the figure TEACHES, not just what it shows."""
    
    def _get_codegen_system_prompt(self) -> str:
        return """You are an expert Three.js developer specializing in educational 3D visualizations.

Your code is:
- Geometrically accurate
- Educationally clear
- Performant and responsive
- Well-commented
- Uses modern Three.js patterns

You generate COMPLETE, working HTML files that can be opened directly in a browser."""
    
    def _validate_code(self, html_code: str) -> Dict:
        """Validate generated code"""
        checks = {
            'has_threejs_import': 'three.min.js' in html_code or 'three.js' in html_code,
            'has_scene': 'new THREE.Scene()' in html_code,
            'has_camera': 'Camera' in html_code,
            'has_renderer': 'WebGLRenderer' in html_code,
            'has_controls': 'Controls' in html_code,
            'has_animation': 'requestAnimationFrame' in html_code or 'animate' in html_code,
            'has_canvas': '<canvas' in html_code or 'renderer.domElement' in html_code
        }
        
        return {
            'valid': all(checks.values()),
            'checks': checks,
            'warnings': [k for k, v in checks.items() if not v]
        }
    
    def _fallback_template(self, figure_id: str, edu_context: EducationalContext) -> str:
        """Simple fallback if generation fails"""
        return f"""<!DOCTYPE html>
<html>
<head>
    <title>{edu_context.concept}</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body>
    <div id="info">
        <h3>{edu_context.concept}</h3>
        <p>{edu_context.learning_objective}</p>
        <p><em>Fallback template - regeneration needed</em></p>
    </div>
    <script>
        // Basic scene setup
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer();
        
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);
        
        // Placeholder cube
        const geometry = new THREE.BoxGeometry();
        const material = new THREE.MeshBasicMaterial({{color: 0x00ff00}});
        const cube = new THREE.Mesh(geometry, material);
        scene.add(cube);
        
        camera.position.z = 5;
        
        function animate() {{
            requestAnimationFrame(animate);
            cube.rotation.x += 0.01;
            cube.rotation.y += 0.01;
            renderer.render(scene, camera);
        }}
        animate();
    </script>
</body>
</html>"""


def main():
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python sophisticated_3d_converter.py <chapter> <figure_path> [figure_id]")
        print("\nExample: python sophisticated_3d_converter.py imaging figures/imaging/pinhole_geometry2.png fig-pinholeGeometry")
        print("\nRequires: OPENAI_API_KEY environment variable")
        sys.exit(1)
    
    chapter = sys.argv[1]
    figure_path = Path(sys.argv[2])
    figure_id = sys.argv[3] if len(sys.argv) > 3 else figure_path.stem
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ OPENAI_API_KEY not set. This converter requires GPT-4V.")
        sys.exit(1)
    
    converter = Sophisticated3DConverter(chapter)
    result = converter.convert_figure(figure_path, figure_id)
    
    print(f"\n{'='*70}")
    print("✅ CONVERSION COMPLETE")
    print(f"{'='*70}")
    print(f"Output: {result['html_path']}")
    print(f"Quality: {'✓' if result['code_quality']['valid'] else '⚠️'}")
    print(f"\nEducational Context:")
    print(f"  Concept: {result['educational_context']['concept']}")
    print(f"  Key terms: {', '.join(result['educational_context']['key_terms'][:5])}")


if __name__ == '__main__':
    main()
