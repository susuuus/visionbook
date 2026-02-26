#!/usr/bin/env python3
"""
Multi-Agent Figure Classification and Processing Pipeline

Implements agentic workflow with specialized agents:
- ExtractorAgent: Parses .qmd files, extracts figure context
- AnalyzerAgent: Performs visual analysis on images
- ClassifierAgent: LLM-based classification with reasoning
- VerifierAgent: Cross-validates classifications
- CoordinatorAgent: Orchestrates workflow, resolves conflicts
- ConverterAgent: Plans and executes 3D conversions

Each agent has tools, memory, and can communicate via shared state.
"""

import json
import re
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Any, Tuple
from enum import Enum
import numpy as np
from PIL import Image
from abc import ABC, abstractmethod


# ============================================================================
# Shared Memory and Communication Protocol
# ============================================================================

class MessageType(Enum):
    REQUEST = "request"
    RESPONSE = "response"
    QUERY = "query"
    VERIFICATION = "verification"
    DISPUTE = "dispute"
    DECISION = "decision"


@dataclass
class AgentMessage:
    """Message passed between agents"""
    sender: str
    receiver: str
    msg_type: MessageType
    content: Dict[str, Any]
    timestamp: float = field(default_factory=lambda: __import__('time').time())
    

@dataclass
class FigureContext:
    """Shared state for a figure across agents"""
    filename: str
    filepath: Path
    
    # From ExtractorAgent
    caption: Optional[str] = None
    metadata: Optional[str] = None
    surrounding_text: Optional[str] = None
    layout_group: Optional[str] = None
    
    # From AnalyzerAgent
    image_properties: Optional[Dict] = None
    visual_analysis: Optional[Dict] = None
    
    # From ClassifierAgent
    classification: Optional[str] = None
    classification_reason: Optional[str] = None
    classification_confidence: float = 0.0
    
    # From VerifierAgent
    verified: bool = False
    verification_notes: Optional[str] = None
    disputes: List[str] = field(default_factory=list)
    
    # From ConverterAgent
    conversion_plan: Optional[Dict] = None
    converted: bool = False
    
    # Message history
    message_history: List[AgentMessage] = field(default_factory=list)


class SharedMemory:
    """Shared memory across all agents"""
    def __init__(self):
        self.figures: Dict[str, FigureContext] = {}
        self.global_stats: Dict[str, Any] = {}
        self.agent_states: Dict[str, Dict] = {}
        self.message_queue: List[AgentMessage] = []
        
    def update_figure(self, filename: str, **kwargs):
        if filename not in self.figures:
            raise KeyError(f"Figure {filename} not in memory")
        for key, value in kwargs.items():
            setattr(self.figures[filename], key, value)
            
    def add_message(self, msg: AgentMessage):
        self.message_queue.append(msg)
        if msg.content.get('figure'):
            fig = msg.content['figure']
            if fig in self.figures:
                self.figures[fig].message_history.append(msg)


# ============================================================================
# Base Agent Class with Tool Use
# ============================================================================

class BaseAgent(ABC):
    """Base class for all agents with tool use capabilities"""
    
    def __init__(self, name: str, memory: SharedMemory):
        self.name = name
        self.memory = memory
        self.tools = self._register_tools()
        self.agent_state = {}
        
    @abstractmethod
    def _register_tools(self) -> Dict[str, callable]:
        """Register tools this agent can use"""
        pass
    
    @abstractmethod
    def process(self, input_data: Any) -> Any:
        """Main processing method - agent's core task"""
        pass
    
    def send_message(self, receiver: str, msg_type: MessageType, content: Dict):
        """Send message to another agent"""
        msg = AgentMessage(
            sender=self.name,
            receiver=receiver,
            msg_type=msg_type,
            content=content
        )
        self.memory.add_message(msg)
        return msg
    
    def receive_messages(self, msg_type: Optional[MessageType] = None) -> List[AgentMessage]:
        """Receive messages addressed to this agent"""
        messages = [m for m in self.memory.message_queue 
                   if m.receiver == self.name]
        if msg_type:
            messages = [m for m in messages if m.msg_type == msg_type]
        return messages
    
    def use_tool(self, tool_name: str, **kwargs) -> Any:
        """Execute a tool"""
        if tool_name not in self.tools:
            raise ValueError(f"Tool {tool_name} not available for {self.name}")
        return self.tools[tool_name](**kwargs)
    
    def log(self, message: str, level: str = "INFO"):
        """Log agent activity"""
        print(f"[{self.name}] {level}: {message}")


# ============================================================================
# Specialized Agents
# ============================================================================

class ExtractorAgent(BaseAgent):
    """Extracts figure references and context from .qmd files"""
    
    def _register_tools(self) -> Dict[str, callable]:
        return {
            'parse_qmd': self._parse_qmd_file,
            'extract_caption': self._extract_caption,
            'extract_layout_groups': self._extract_layout_groups,
            'get_surrounding_context': self._get_surrounding_context
        }
    
    def process(self, qmd_file: Path, chapter: str) -> List[FigureContext]:
        """Extract all figure contexts from .qmd file"""
        self.log(f"Extracting figures from {qmd_file}")
        
        content = self.use_tool('parse_qmd', filepath=qmd_file)
        figure_refs = self._find_figure_references(content, chapter)
        layout_groups = self.use_tool('extract_layout_groups', content=content, chapter=chapter)
        
        contexts = []
        for fig_name in figure_refs:
            ctx = FigureContext(
                filename=fig_name,
                filepath=Path(f"figures/{chapter}/{fig_name}")
            )
            
            # Extract context using tools
            ctx.caption = self.use_tool('extract_caption', 
                                       content=content, 
                                       filename=fig_name)
            ctx.surrounding_text = self.use_tool('get_surrounding_context',
                                                content=content,
                                                filename=fig_name)
            
            # Check if in layout group
            for group_id, figs in layout_groups.items():
                if fig_name in figs:
                    ctx.layout_group = group_id
                    
            contexts.append(ctx)
            self.memory.figures[fig_name] = ctx
            
        self.log(f"Extracted {len(contexts)} figures with context")
        return contexts
    
    def _parse_qmd_file(self, filepath: Path) -> str:
        with open(filepath, 'r') as f:
            return f.read()
    
    def _find_figure_references(self, content: str, chapter: str) -> List[str]:
        pattern = rf'figures/{chapter}/([a-zA-Z0-9_.-]+\.(?:png|jpg|JPG))'
        matches = re.findall(pattern, content)
        return list(set(matches))
    
    def _extract_caption(self, content: str, filename: str) -> str:
        pattern = rf'!\[([^\]]*)\]\([^)]*{re.escape(filename)}\)'
        match = re.search(pattern, content)
        return match.group(1).strip() if match else ""
    
    def _extract_layout_groups(self, content: str, chapter: str) -> Dict[str, List[str]]:
        groups = {}
        pattern = r':::\{layout-[^}]+#(fig-[^\}]+)\}(.*?):::'
        for match in re.finditer(pattern, content, re.DOTALL):
            fig_id = match.group(1)
            block_content = match.group(2)
            fig_pattern = rf'figures/{chapter}/([a-zA-Z0-9_.-]+\.(?:png|jpg|JPG))'
            figs_in_block = re.findall(fig_pattern, block_content)
            if figs_in_block:
                groups[fig_id] = figs_in_block
        return groups
    
    def _get_surrounding_context(self, content: str, filename: str) -> str:
        pattern = rf'([^\n]{{0,300}})\n[^\n]*{re.escape(filename)}'
        match = re.search(pattern, content)
        return match.group(1).strip() if match else ""


class AnalyzerAgent(BaseAgent):
    """Performs visual analysis on images"""
    
    def _register_tools(self) -> Dict[str, callable]:
        return {
            'load_image': self._load_image,
            'compute_color_stats': self._compute_color_stats,
            'compute_variance': self._compute_variance,
            'detect_composition': self._detect_composition,
            'estimate_complexity': self._estimate_complexity
        }
    
    def process(self, figure_ctx: FigureContext) -> Dict[str, Any]:
        """Analyze image and return properties"""
        self.log(f"Analyzing {figure_ctx.filename}")
        
        try:
            img, img_array = self.use_tool('load_image', filepath=figure_ctx.filepath)
        except Exception as e:
            self.log(f"Failed to load {figure_ctx.filename}: {e}", "ERROR")
            return {'error': str(e)}
        
        analysis = {
            'dimensions': img.size,
            'mode': img.mode,
            'color_stats': self.use_tool('compute_color_stats', img_array=img_array),
            'variance_map': self.use_tool('compute_variance', img_array=img_array),
            'composition': self.use_tool('detect_composition', img_array=img_array),
            'complexity': self.use_tool('estimate_complexity', img_array=img_array)
        }
        
        # Store in memory
        self.memory.update_figure(figure_ctx.filename, 
                                 image_properties=analysis,
                                 visual_analysis=self._interpret_analysis(analysis))
        
        return analysis
    
    def _load_image(self, filepath: Path) -> Tuple[Image.Image, np.ndarray]:
        img = Image.open(filepath)
        return img, np.array(img)
    
    def _compute_color_stats(self, img_array: np.ndarray) -> Dict:
        if len(img_array.shape) == 3:
            reshaped = img_array[:,:,:3].reshape(-1, 3)
            unique_colors = len(np.unique(reshaped, axis=0))
        else:
            unique_colors = len(np.unique(img_array))
        return {'unique_colors': unique_colors}
    
    def _compute_variance(self, img_array: np.ndarray) -> Dict:
        gray = np.mean(img_array[:,:,:3], axis=2) if len(img_array.shape) == 3 else img_array
        local_vars = []
        h, w = gray.shape
        for i in range(0, min(h, 200), 10):
            for j in range(0, min(w, 200), 10):
                patch = gray[i:min(i+10, h), j:min(j+10, w)]
                if patch.size > 0:
                    local_vars.append(np.var(patch))
        return {
            'mean_variance': float(np.mean(local_vars)) if local_vars else 0,
            'variance_std': float(np.std(local_vars)) if local_vars else 0
        }
    
    def _detect_composition(self, img_array: np.ndarray) -> Dict:
        """Detect if image is composite (multi-panel)"""
        h, w = img_array.shape[:2]
        aspect_ratio = w / h
        is_wide_panel = aspect_ratio > 2.5
        is_tall_panel = aspect_ratio < 0.4
        return {
            'aspect_ratio': float(aspect_ratio),
            'likely_composite': is_wide_panel or is_tall_panel,
            'layout_hint': 'horizontal' if is_wide_panel else 'vertical' if is_tall_panel else 'single'
        }
    
    def _estimate_complexity(self, img_array: np.ndarray) -> Dict:
        """Estimate visual complexity"""
        # Simple edge density as complexity measure
        gray = np.mean(img_array[:,:,:3], axis=2) if len(img_array.shape) == 3 else img_array
        # Sobel-like edge detection
        dy = np.diff(gray, axis=0)
        dx = np.diff(gray, axis=1)
        edge_density = (np.abs(dy).mean() + np.abs(dx).mean()) / 2
        return {
            'edge_density': float(edge_density),
            'complexity_level': 'high' if edge_density > 30 else 'medium' if edge_density > 10 else 'low'
        }
    
    def _interpret_analysis(self, analysis: Dict) -> Dict:
        """Interpret raw analysis into insights"""
        colors = analysis['color_stats']['unique_colors']
        variance = analysis['variance_map']['mean_variance']
        composition = analysis['composition']
        
        return {
            'is_photograph_likely': colors > 10000 and variance > 500,
            'is_diagram_likely': colors < 2000 and variance < 300,
            'is_composite': composition['likely_composite'],
            'visual_type': self._classify_visual_type(colors, variance, composition)
        }
    
    def _classify_visual_type(self, colors: int, variance: float, composition: Dict) -> str:
        if composition['likely_composite']:
            return 'composite_figure'
        elif colors > 10000 and variance > 500:
            return 'photograph'
        elif colors < 500:
            return 'simple_diagram'
        elif colors < 2000:
            return 'complex_diagram'
        else:
            return 'rendered_or_mixed'


class ClassifierAgent(BaseAgent):
    """LLM-based classifier with reasoning"""
    
    def _register_tools(self) -> Dict[str, callable]:
        return {
            'query_llm': self._query_llm,
            'extract_keywords': self._extract_keywords,
            'match_patterns': self._match_patterns
        }
    
    def process(self, figure_ctx: FigureContext) -> Tuple[str, str, float]:
        """Classify figure using LLM reasoning"""
        self.log(f"Classifying {figure_ctx.filename}")
        
        # Gather all available context
        context = self._build_classification_context(figure_ctx)
        
        # Query LLM for classification
        classification_result = self.use_tool('query_llm', context=context)
        
        # Update memory
        self.memory.update_figure(
            figure_ctx.filename,
            classification=classification_result['category'],
            classification_reason=classification_result['reasoning'],
            classification_confidence=classification_result['confidence']
        )
        
        # Send verification request
        self.send_message(
            receiver='VerifierAgent',
            msg_type=MessageType.VERIFICATION,
            content={
                'figure': figure_ctx.filename,
                'classification': classification_result
            }
        )
        
        return (classification_result['category'], 
                classification_result['reasoning'],
                classification_result['confidence'])
    
    def _build_classification_context(self, fig_ctx: FigureContext) -> Dict:
        """Build rich context for LLM"""
        return {
            'filename': fig_ctx.filename,
            'caption': fig_ctx.caption or 'N/A',
            'surrounding_text': fig_ctx.surrounding_text or 'N/A',
            'layout_group': fig_ctx.layout_group or 'None',
            'visual_analysis': fig_ctx.visual_analysis or {},
            'image_properties': fig_ctx.image_properties or {}
        }
    
    def _query_llm(self, context: Dict) -> Dict:
        """Query LLM for classification (placeholder for actual LLM call)"""
        
        # This is where you'd call actual LLM (OpenAI, Claude, etc.)
        # For now, implement rule-based reasoning that mimics LLM
        
        prompt = self._build_llm_prompt(context)
        
        # PLACEHOLDER: Simulate LLM reasoning
        # In production, replace with: response = openai.chat.completions.create(...)
        reasoning_result = self._simulate_llm_reasoning(context)
        
        return reasoning_result
    
    def _build_llm_prompt(self, context: Dict) -> str:
        return f"""Analyze this figure and classify it:

FILENAME: {context['filename']}
CAPTION: {context['caption']}
CONTEXT: {context['surrounding_text']}

VISUAL ANALYSIS:
- Colors: {context['visual_analysis'].get('visual_type', 'unknown')}
- Complexity: {context['image_properties'].get('complexity', {}).get('complexity_level', 'unknown')}
- Composition: {context['image_properties'].get('composition', {}).get('layout_hint', 'unknown')}

CLASSIFICATION OPTIONS:
1. photograph - Real-world photos
2. diagrams_2d - Simple 2D illustrations
3. diagrams_3d_candidates - 3D geometric concepts (camera geometry, projections, etc.)
4. composite_teaching - Multi-panel teaching figures

Provide: category, reasoning, confidence (0-1)"""
    
    def _simulate_llm_reasoning(self, context: Dict) -> Dict:
        """Simulate LLM reasoning with rules (replace with real LLM)"""
        
        filename = context['filename'].lower()
        caption = context['caption'].lower()
        text = context['surrounding_text'].lower()
        visual = context['visual_analysis']
        
        # Check for 3D keywords
        keywords_3d = ['projection', 'orthographic', 'perspective', 'pinhole', 'geometry', 
                       'coordinate', 'camera', 'brdf', 'ray', 'lens']
        has_3d_concept = any(kw in filename or kw in caption or kw in text 
                            for kw in keywords_3d)
        
        # Check composition
        is_composite = visual.get('is_composite', False)
        is_photo_like = visual.get('is_photograph_likely', False)
        is_diagram_like = visual.get('is_diagram_likely', False)
        
        # Reasoning
        if is_composite and has_3d_concept:
            return {
                'category': 'composite_teaching',
                'reasoning': f"Composite figure teaching 3D concept. Caption mentions geometric principles.",
                'confidence': 0.85
            }
        elif has_3d_concept and (is_diagram_like or filename in ['straw_camera', 'no_picture']):
            return {
                'category': 'diagrams_3d_candidates',
                'reasoning': f"Contains 3D geometric concept keywords. Visual analysis suggests diagram.",
                'confidence': 0.9
            }
        elif is_photo_like and not has_3d_concept:
            return {
                'category': 'photograph',
                'reasoning': "High color count and variance suggest photograph. No 3D geometry concepts.",
                'confidence': 0.85
            }
        elif is_diagram_like:
            return {
                'category': 'diagrams_2d',
                'reasoning': "Low complexity, limited colors, no 3D concepts.",
                'confidence': 0.8
            }
        else:
            return {
                'category': 'unknown',
                'reasoning': "Unclear classification from available evidence.",
                'confidence': 0.5
            }
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extract key terms from text"""
        keywords = ['projection', 'camera', 'geometry', 'coordinate', 'pinhole', 
                   'orthographic', 'perspective', 'brdf', 'ray', 'lens']
        return [kw for kw in keywords if kw in text.lower()]
    
    def _match_patterns(self, filename: str, patterns: List[str]) -> bool:
        """Check if filename matches any pattern"""
        return any(p in filename.lower() for p in patterns)


class VerifierAgent(BaseAgent):
    """Cross-validates classifications and identifies disputes"""
    
    def _register_tools(self) -> Dict[str, callable]:
        return {
            'check_consistency': self._check_consistency,
            'cross_reference': self._cross_reference,
            'raise_dispute': self._raise_dispute
        }
    
    def process(self, figure_ctx: FigureContext) -> Dict:
        """Verify classification"""
        self.log(f"Verifying {figure_ctx.filename}")
        
        # Check consistency across different signals
        consistency = self.use_tool('check_consistency', figure_ctx=figure_ctx)
        
        if consistency['is_consistent']:
            self.memory.update_figure(
                figure_ctx.filename,
                verified=True,
                verification_notes=consistency['notes']
            )
            self.log(f"✓ Verified {figure_ctx.filename} as {figure_ctx.classification}")
        else:
            # Raise dispute
            self.use_tool('raise_dispute', 
                         figure_ctx=figure_ctx,
                         reason=consistency['conflict_reason'])
            self.log(f"⚠ Dispute raised for {figure_ctx.filename}", "WARNING")
        
        return consistency
    
    def _check_consistency(self, figure_ctx: FigureContext) -> Dict:
        """Check if classification matches evidence"""
        classification = figure_ctx.classification
        visual = figure_ctx.visual_analysis or {}
        
        conflicts = []
        
        # Check photo classification
        if classification == 'photograph':
            if not visual.get('is_photograph_likely', False):
                conflicts.append("Classified as photo but visual analysis suggests diagram")
        
        # Check 3D candidate
        elif classification == 'diagrams_3d_candidates':
            caption = (figure_ctx.caption or '').lower()
            if 'projection' not in caption and 'camera' not in caption and 'geometry' not in caption:
                conflicts.append("Classified as 3D but no geometric keywords in caption")
        
        # Check composite
        elif classification == 'composite_teaching':
            if not visual.get('is_composite', False):
                conflicts.append("Classified as composite but composition analysis disagrees")
        
        is_consistent = len(conflicts) == 0
        
        return {
            'is_consistent': is_consistent,
            'conflicts': conflicts,
            'conflict_reason': '; '.join(conflicts) if conflicts else None,
            'notes': 'All checks passed' if is_consistent else 'Conflicts detected'
        }
    
    def _cross_reference(self, figure_ctx: FigureContext) -> Dict:
        """Cross-reference with similar figures"""
        # Check if other figures in same layout group have similar classification
        if figure_ctx.layout_group:
            group_figs = [f for f in self.memory.figures.values() 
                         if f.layout_group == figure_ctx.layout_group]
            classifications = [f.classification for f in group_figs if f.classification]
            return {'group_classifications': classifications}
        return {}
    
    def _raise_dispute(self, figure_ctx: FigureContext, reason: str):
        """Raise dispute to Coordinator"""
        self.memory.update_figure(
            figure_ctx.filename,
            verified=False,
            disputes=[reason]
        )
        
        self.send_message(
            receiver='CoordinatorAgent',
            msg_type=MessageType.DISPUTE,
            content={
                'figure': figure_ctx.filename,
                'reason': reason,
                'current_classification': figure_ctx.classification
            }
        )


class CoordinatorAgent(BaseAgent):
    """Orchestrates workflow and resolves disputes"""
    
    def _register_tools(self) -> Dict[str, callable]:
        return {
            'resolve_dispute': self._resolve_dispute,
            'reprocess_figure': self._reprocess_figure,
            'finalize_classification': self._finalize_classification
        }
    
    def __init__(self, name: str, memory: SharedMemory):
        super().__init__(name, memory)
        self.agents = {}  # Will be populated with agent references
        
    def register_agent(self, agent: BaseAgent):
        """Register other agents for coordination"""
        self.agents[agent.name] = agent
        
    def process(self, figures: List[FigureContext]) -> Dict:
        """Orchestrate full pipeline"""
        self.log("Starting coordinated pipeline")
        
        results = {
            'photograph': [],
            'photographs': [],  # Alias for backwards compatibility
            'diagrams_2d': [],
            'diagrams_3d_candidates': [],
            'composite_teaching': [],
            'unknown': [],
            'disputes': []
        }
        
        # Process each figure through agent pipeline
        for fig_ctx in figures:
            self.log(f"Processing {fig_ctx.filename}")
            
            # 1. Analyzer
            if 'AnalyzerAgent' in self.agents:
                self.agents['AnalyzerAgent'].process(fig_ctx)
            
            # 2. Classifier
            if 'ClassifierAgent' in self.agents:
                self.agents['ClassifierAgent'].process(fig_ctx)
            
            # 3. Verifier
            if 'VerifierAgent' in self.agents:
                self.agents['VerifierAgent'].process(fig_ctx)
            
            # 4. Handle any disputes
            disputes = self.receive_messages(msg_type=MessageType.DISPUTE)
            for dispute in disputes:
                if dispute.content['figure'] == fig_ctx.filename:
                    resolution = self.use_tool('resolve_dispute', 
                                              figure_ctx=fig_ctx,
                                              dispute=dispute)
                    results['disputes'].append(resolution)
            
            # 5. Finalize
            category = self.use_tool('finalize_classification', figure_ctx=fig_ctx)
            results[category].append(fig_ctx)
        
        # Consolidate photograph/photographs
        results['photographs'].extend(results['photograph'])
        del results['photograph']
        
        self.log(f"Pipeline complete. Processed {len(figures)} figures")
        return results
    
    def _resolve_dispute(self, figure_ctx: FigureContext, dispute: AgentMessage) -> Dict:
        """Resolve classification dispute"""
        self.log(f"Resolving dispute for {figure_ctx.filename}")
        
        # Gather all evidence
        evidence = {
            'visual': figure_ctx.visual_analysis,
            'context': {
                'caption': figure_ctx.caption,
                'text': figure_ctx.surrounding_text
            },
            'current_classification': figure_ctx.classification,
            'dispute_reason': dispute.content['reason']
        }
        
        # Make executive decision
        # In a real system, this could query a more powerful LLM or human
        decision = self._make_executive_decision(evidence)
        
        # Update classification if needed
        if decision['override']:
            self.memory.update_figure(
                figure_ctx.filename,
                classification=decision['new_classification'],
                classification_reason=decision['reasoning'],
                verified=True
            )
        
        return decision
    
    def _make_executive_decision(self, evidence: Dict) -> Dict:
        """Make final decision on disputed classification"""
        # Simple heuristic: trust visual analysis over keywords for composite figures
        visual = evidence['visual']
        current = evidence['current_classification']
        
        if visual and visual.get('is_composite'):
            return {
                'override': current != 'composite_teaching',
                'new_classification': 'composite_teaching',
                'reasoning': 'Executive decision: Visual evidence shows composite structure'
            }
        
        return {
            'override': False,
            'reasoning': 'Current classification stands'
        }
    
    def _reprocess_figure(self, figure_ctx: FigureContext):
        """Reprocess a figure through pipeline"""
        # Trigger re-analysis
        if 'ClassifierAgent' in self.agents:
            self.agents['ClassifierAgent'].process(figure_ctx)
    
    def _finalize_classification(self, figure_ctx: FigureContext) -> str:
        """Finalize and return category"""
        if not figure_ctx.classification:
            return 'unknown'
        return figure_ctx.classification


# ============================================================================
# Pipeline Orchestration
# ============================================================================

class AgenticFigurePipeline:
    """Main pipeline orchestrating all agents"""
    
    def __init__(self, chapter_name: str):
        self.chapter = chapter_name
        self.memory = SharedMemory()
        
        # Initialize all agents
        self.extractor = ExtractorAgent('ExtractorAgent', self.memory)
        self.analyzer = AnalyzerAgent('AnalyzerAgent', self.memory)
        self.classifier = ClassifierAgent('ClassifierAgent', self.memory)
        self.verifier = VerifierAgent('VerifierAgent', self.memory)
        self.coordinator = CoordinatorAgent('CoordinatorAgent', self.memory)
        
        # Register agents with coordinator
        self.coordinator.register_agent(self.extractor)
        self.coordinator.register_agent(self.analyzer)
        self.coordinator.register_agent(self.classifier)
        self.coordinator.register_agent(self.verifier)
        
    def run(self, qmd_file: Path) -> Dict:
        """Run full agentic pipeline"""
        print("="*70)
        print("🤖 AGENTIC FIGURE CLASSIFICATION PIPELINE")
        print("="*70)
        print(f"Chapter: {self.chapter}")
        print(f"Agents: Extractor → Analyzer → Classifier → Verifier → Coordinator")
        print("="*70)
        print()
        
        # Phase 1: Extraction
        print("📄 Phase 1: Context Extraction")
        figure_contexts = self.extractor.process(qmd_file, self.chapter)
        print(f"   Extracted {len(figure_contexts)} figures\n")
        
        # Phase 2: Multi-agent processing with coordination
        print("🔄 Phase 2: Multi-Agent Analysis & Classification")
        results = self.coordinator.process(figure_contexts)
        
        # Phase 3: Summary and reporting
        print("\n" + "="*70)
        print("📊 RESULTS")
        print("="*70)
        for category, figs in results.items():
            if category != 'disputes' and figs:
                print(f"{category}: {len(figs)} figures")
                for fig in figs[:3]:  # Show first 3
                    status = "✓" if fig.verified else "?"
                    print(f"  {status} {fig.filename}")
                if len(figs) > 3:
                    print(f"  ... and {len(figs)-3} more")
        
        if results.get('disputes'):
            print(f"\n⚠️  {len(results['disputes'])} disputes resolved by Coordinator")
        
        print("\n" + "="*70)
        
        # Save results
        self._save_results(results)
        
        return results
    
    def _save_results(self, results: Dict):
        """Save classification results"""
        output_dir = Path(f"figures_sorted/{self.chapter}")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = output_dir / "agentic_classification_results.json"
        
        # Convert to serializable format
        serializable_results = {}
        for category, figs in results.items():
            if category == 'disputes':
                serializable_results[category] = results[category]
            else:
                serializable_results[category] = [
                    {
                        'filename': fig.filename,
                        'classification': fig.classification,
                        'reasoning': fig.classification_reason,
                        'confidence': fig.classification_confidence,
                        'verified': fig.verified,
                        'visual_analysis': fig.visual_analysis,
                        'caption': fig.caption
                    }
                    for fig in figs
                ]
        
        with open(output_file, 'w') as f:
            json.dump(serializable_results, f, indent=2)
        
        print(f"✓ Results saved to {output_file}")


# ============================================================================
# Main Entry Point
# ============================================================================

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python agentic_figure_pipeline.py <chapter_name>")
        print("\nExample: python agentic_figure_pipeline.py imaging")
        sys.exit(1)
    
    chapter = sys.argv[1]
    qmd_file = Path(f"{chapter}.qmd")
    
    if not qmd_file.exists():
        print(f"Error: {qmd_file} not found")
        sys.exit(1)
    
    pipeline = AgenticFigurePipeline(chapter)
    results = pipeline.run(qmd_file)
    
    print(f"\n✅ Agentic pipeline completed for {chapter}")


if __name__ == '__main__':
    main()
