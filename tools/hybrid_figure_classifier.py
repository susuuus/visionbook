#!/usr/bin/env python3
"""
Hybrid Figure Classification Pipeline
- Fast rule-based classification for obvious cases
- LLM reasoning for uncertain/unknown figures
- Conversion planning with LLM
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass
import numpy as np
from PIL import Image
import sys

# Import the rule-based organizer
sys.path.append(str(Path(__file__).parent))
from organize_figures import FigureOrganizer


@dataclass
class LLMConfig:
    """Configuration for LLM usage"""
    provider: str = "openai"  # or "anthropic"
    model: str = "gpt-4o-mini"  # cost-effective model
    api_key: Optional[str] = None
    confidence_threshold: float = 0.7  # Only use LLM if rule-based confidence < this


class HybridClassifier:
    """Combines rule-based + LLM classification"""
    
    def __init__(self, chapter: str, use_llm: bool = True):
        self.chapter = chapter
        self.organizer = FigureOrganizer(chapter)
        self.use_llm = use_llm and self._check_llm_available()
        
        if self.use_llm:
            self.llm_config = LLMConfig(api_key=os.getenv("OPENAI_API_KEY"))
            self._init_llm()
    
    def _check_llm_available(self) -> bool:
        """Check if LLM API is available"""
        return os.getenv("OPENAI_API_KEY") is not None or os.getenv("ANTHROPIC_API_KEY") is not None
    
    def _init_llm(self):
        """Initialize LLM client"""
        if self.llm_config.provider == "openai":
            try:
                import openai
                self.llm_client = openai.OpenAI(api_key=self.llm_config.api_key)
            except ImportError:
                print("⚠️  OpenAI not installed. Run: pip install openai")
                self.use_llm = False
        elif self.llm_config.provider == "anthropic":
            try:
                import anthropic
                self.llm_client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
            except ImportError:
                print("⚠️  Anthropic not installed. Run: pip install anthropic")
                self.use_llm = False
    
    def classify_figures(self) -> Dict:
        """Hybrid classification pipeline"""
        
        print("="*70)
        print("🤖 HYBRID CLASSIFICATION PIPELINE")
        print("="*70)
        print(f"Chapter: {self.chapter}")
        print(f"LLM enabled: {self.use_llm}")
        print("="*70)
        
        # Phase 1: Rule-based classification
        print("\n📊 Phase 1: Rule-based classification")
        results = self.organizer.organize_and_classify()
        
        # Extract uncertain classifications
        uncertain = []
        for category, figures in results.items():
            for fig in figures:
                # If figure has low confidence or is unknown
                if category == 'unknown' or fig.get('confidence', 1.0) < self.llm_config.confidence_threshold:
                    uncertain.append(fig)
        
        print(f"   ✓ {len(results.get('photographs', []))} photographs")
        print(f"   ✓ {len(results.get('diagrams_2d', []))} 2D diagrams")
        print(f"   ✓ {len(results.get('diagrams_3d_candidates', []))} 3D candidates")
        print(f"   ⚠️  {len(uncertain)} uncertain figures")
        
        # Phase 2: LLM refinement for uncertain cases
        if self.use_llm and uncertain:
            print(f"\n🧠 Phase 2: LLM refinement for {len(uncertain)} uncertain figures")
            
            reclassified = 0
            for fig in uncertain:
                new_classification = self._llm_classify(fig)
                
                if new_classification and new_classification['confidence'] > self.llm_config.confidence_threshold:
                    # Move figure to new category
                    old_cat = fig.get('category', 'unknown')
                    new_cat = new_classification['category']
                    
                    if old_cat in results:
                        results[old_cat] = [f for f in results[old_cat] if f['filename'] != fig['filename']]
                    
                    if new_cat not in results:
                        results[new_cat] = []
                    
                    fig.update(new_classification)
                    results[new_cat].append(fig)
                    reclassified += 1
                    
                    print(f"   ✓ {fig['filename']}: {old_cat} → {new_cat} ({new_classification['confidence']:.0%})")
            
            print(f"\n   Reclassified: {reclassified}/{len(uncertain)}")
        
        # Phase 3: Conversion planning for 3D candidates
        if self.use_llm and results.get('diagrams_3d_candidates'):
            print(f"\n🎨 Phase 3: Conversion planning for {len(results['diagrams_3d_candidates'])} 3D candidates")
            
            for fig in results['diagrams_3d_candidates']:
                plan = self._llm_conversion_plan(fig)
                if plan:
                    fig['conversion_plan'] = plan
                    print(f"   ✓ {fig['filename']}: {plan['approach']}")
        
        # Save results
        self._save_results(results)
        
        return results
    
    def _llm_classify(self, figure: Dict) -> Optional[Dict]:
        """Use LLM to classify uncertain figure"""
        
        prompt = self._build_classification_prompt(figure)
        
        try:
            if self.llm_config.provider == "openai":
                response = self.llm_client.chat.completions.create(
                    model=self.llm_config.model,
                    messages=[
                        {"role": "system", "content": self._get_system_prompt()},
                        {"role": "user", "content": prompt}
                    ],
                    response_format={"type": "json_object"},
                    temperature=0.3
                )
                
                result = json.loads(response.choices[0].message.content)
                return result
            
        except Exception as e:
            print(f"   ⚠️  LLM error for {figure['filename']}: {e}")
            return None
    
    def _llm_conversion_plan(self, figure: Dict) -> Optional[Dict]:
        """Generate conversion plan with LLM"""
        
        prompt = f"""This figure is a 3D geometry candidate: {figure['filename']}

Caption: {figure.get('caption', 'N/A')}
Context: {figure.get('surrounding_text', 'N/A')}

Generate a conversion plan for making this interactive 3D.

Provide JSON:
{{
  "approach": "orthographic|perspective|custom",
  "camera_position": [x, y, z],
  "look_at": [x, y, z],
  "elements_to_model": ["list", "of", "3d", "elements"],
  "interaction_type": "orbit|pan|zoom",
  "priority": 1-5
}}"""
        
        try:
            if self.llm_config.provider == "openai":
                response = self.llm_client.chat.completions.create(
                    model=self.llm_config.model,
                    messages=[
                        {"role": "system", "content": "You are a 3D graphics expert planning interactive figure conversions."},
                        {"role": "user", "content": prompt}
                    ],
                    response_format={"type": "json_object"},
                    temperature=0.5
                )
                
                result = json.loads(response.choices[0].message.content)
                return result
                
        except Exception as e:
            print(f"   ⚠️  Conversion planning error: {e}")
            return None
    
    def _build_classification_prompt(self, figure: Dict) -> str:
        """Build prompt for classification"""
        return f"""Classify this computer vision textbook figure:

FILENAME: {figure['filename']}
CAPTION: {figure.get('caption', 'N/A')}
CONTEXT: {figure.get('surrounding_text', 'N/A')}

VISUAL PROPERTIES:
- Color count: {figure.get('colors', 'unknown')}
- Complexity: {figure.get('complexity', 'unknown')}
- Dimensions: {figure.get('width', '?')}x{figure.get('height', '?')}

Classify into:
1. photograph - Real-world photographs
2. diagrams_2d - Simple 2D illustrations/plots
3. diagrams_3d_candidates - Diagrams teaching 3D concepts (camera geometry, projections, coordinates)
4. composite_teaching - Multi-panel teaching figures

Provide JSON:
{{
  "category": "one of the above",
  "reasoning": "why this classification",
  "confidence": 0.0-1.0,
  "key_evidence": ["what indicates this category"]
}}"""
    
    def _get_system_prompt(self) -> str:
        """System prompt for classification"""
        return """You are an expert in computer vision pedagogy and figure classification.

Your task: Classify figures from a computer vision textbook to help:
1. Organize figures by type
2. Identify candidates for interactive 3D conversion
3. Distinguish photographs from diagrams

Key distinctions:
- diagrams_3d_candidates: Show camera geometry, projections, coordinate systems, perspective/orthographic concepts
- composite_teaching: Multi-panel figures teaching concepts (e.g., photo + diagram + labels)
- photographs: Real-world images used as examples
- diagrams_2d: Simple plots, charts, 2D illustrations

Be precise and confident in your classifications."""
    
    def _save_results(self, results: Dict):
        """Save classification results"""
        output_dir = Path(f"figures_sorted/{self.chapter}")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = output_dir / "hybrid_classification_results.json"
        
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n✅ Results saved to {output_file}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python hybrid_figure_classifier.py <chapter_name>")
        print("\nExample: python hybrid_figure_classifier.py imaging")
        print("\nSet OPENAI_API_KEY or ANTHROPIC_API_KEY environment variable to enable LLM")
        sys.exit(1)
    
    chapter = sys.argv[1]
    
    classifier = HybridClassifier(chapter, use_llm=True)
    results = classifier.classify_figures()
    
    print("\n✅ Hybrid classification complete!")


if __name__ == '__main__':
    main()
