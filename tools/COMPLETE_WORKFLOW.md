# Complete Figure Processing System

## 🎯 Universal Design - Works for ANY Chapter!

```bash
# Process any chapter:
python tools/complete_figure_pipeline.py imaging
python tools/complete_figure_pipeline.py color
python tools/complete_figure_pipeline.py lenses
python tools/complete_figure_pipeline.py camera_as_linsys
# ... any chapter in your book!
```

---

## 📋 Pipeline 1: Classification & Organization

### **Workflow:**

```
{chapter}.qmd
    ↓
Phase 1: Extract Figures
  • Parse .qmd for figure references
  • Extract captions, context, surrounding text
    ↓
Phase 2: Analyze Figures
  • Visual analysis (colors, variance, dimensions)
  • Rule-based classification
  • Caption/context keywords
    ↓
Phase 3: LLM Refinement (if API key available)
  • Process only uncertain cases (confidence < 70%)
  • Uses gpt-4o-mini for cost efficiency
  • Semantic understanding of captions
    ↓
Phase 4: Sort into Folders
  • Copy files to: figures_sorted/{chapter}/
    - photographs/
    - diagrams_2d/
    - diagrams_3d_candidates/  ← Key for 3D conversion
    - composite_teaching/
    - unknown/
    ↓
Phase 5: Review & Verification (🆕 Review Agent)
  ✓ Check 1: All figures accounted for?
    - Compare .qmd references vs sorted files
    - Report missing figures
  
  ✓ Check 2: Low confidence classifications?
    - Flag figures with confidence < 60%
  
  ✓ Check 3: LLM category review
    - Sample check each category (first 3 figures)
    - Verify classifications are correct
    - Suggest reclassifications if needed
  
  ✓ Check 4: Unknown rate acceptable?
    - Alert if unknowns > 30%
    ↓
Phase 6: Address Issues (if found)
  • Reclassify misclassified figures
  • Re-process missing figures
  • Move files to correct folders
    ↓
Phase 7: Generate Report
  • classification_report.json with:
    - All classifications
    - Review results
    - 3D conversion candidates list
```

### **Output Structure:**

```
figures_sorted/{chapter}/
├── photographs/
│   ├── photo1.jpg
│   └── photo2.png
├── diagrams_2d/
│   ├── plot1.png
│   └── chart2.png
├── diagrams_3d_candidates/
│   ├── pinhole_geometry2.png
│   ├── orthogonal_projection.png
│   └── similar_triangles2.png
├── composite_teaching/
│   ├── straw_camera.png
│   └── multi_panel_figure.png
├── unknown/
│   └── ambiguous.png
└── classification_report.json
```

### **Report Format:**

```json
{
  "chapter": "imaging",
  "total_figures": 15,
  "llm_used": true,
  "summary": {
    "photographs": 0,
    "diagrams_2d": 2,
    "diagrams_3d_candidates": 3,
    "composite_teaching": 4,
    "unknown": 6
  },
  "3d_conversion_ready": [
    "orthogonal_projection.png",
    "pinhole_geometry2.png",
    "similar_triangles2.png"
  ],
  "review": {
    "issues_found": true,
    "issues": [
      {
        "type": "misclassification",
        "figure": "some_figure.png",
        "current_category": "diagrams_2d",
        "suggested_category": "diagrams_3d_candidates",
        "reason": "Contains camera geometry concepts"
      }
    ],
    "total_checked": 15,
    "all_accounted": true
  }
}
```

---

## 🎨 Pipeline 2: 3D Conversion

### **Workflow:**

```
classification_report.json
    ↓
Load 3D Candidates List
    ↓
FOR EACH candidate in diagrams_3d_candidates/
    ↓
  Stage 1: Educational Context (LLM)
    • What concept is being taught?
    • Learning objectives
    • Related equations
    • Key terms
    ↓
  Stage 2: Geometric Analysis (GPT-4V)
    • Vision model parses diagram
    • Identifies all 3D elements:
      - Planes, lines, points
      - Cameras, coordinate systems
      - Rays, frustums
    • Extracts spatial relationships
    • Maps visual properties
    ↓
  Stage 3: Conversion Planning (LLM)
    • Scene graph design
    • Three.js geometries/materials
    • Camera strategy
    • Animation plan
    • Educational enhancements
    ↓
  Stage 4: Code Generation (LLM)
    • Complete Three.js HTML
    • Accurate geometry
    • Interactive controls
    • Educational UI
    ↓
  Stage 5: Validation
    • Check for required Three.js components
    • Report quality metrics
    ↓
Save to interactive_figures/{chapter}/
    ↓
Generate Index Gallery
```

### **Output Structure:**

```
interactive_figures/{chapter}/
├── fig-orthographics_3d.html
├── fig-pinholeGeometry2_3d.html
├── fig-similarTriangles_3d.html
├── index.html  ← Gallery with all figures
└── conversion_report.json
```

---

## 🔍 Review Agent Details

The review agent ensures **completeness** and **accuracy**:

### **1. Completeness Check**
```python
# Ensures ALL figures from .qmd are sorted
original_figures = extract_from_qmd()  # 15 figures
sorted_figures = count_in_folders()     # Should be 15

if missing:
    ALERT: "Missing 2 figures: [fig1.png, fig2.png]"
    ACTION: Re-process missing figures
```

### **2. Accuracy Check**
```python
# LLM reviews sample of each category
for category in [photos, 2d, 3d, composite]:
    sample = category[:3]  # First 3 figures
    
    for figure in sample:
        llm_review(figure, current_category)
        
        if misclassified:
            ALERT: "figure.png: 2d → 3d_candidate"
            ACTION: Move to correct folder
```

### **3. Confidence Check**
```python
low_confidence = [f for f in figures if f.confidence < 0.6]

if low_confidence:
    ALERT: "5 figures need LLM refinement"
    ACTION: Send to LLM for reclassification
```

### **4. Unknown Rate Check**
```python
if unknowns > 30%:
    WARNING: "High unknown rate - need better rules or LLM"
```

---

## 💡 Usage Examples

### Process Single Chapter:
```bash
export OPENAI_API_KEY="sk-..."
python tools/complete_figure_pipeline.py imaging
```

### Process Multiple Chapters:
```bash
for chapter in imaging color lenses optical_flow; do
    python tools/complete_figure_pipeline.py $chapter
done
```

### Then Convert 3D Figures:
```bash
python tools/threejs_conversion_pipeline.py imaging
```

### Batch Process Everything:
```bash
# Create wrapper script
python tools/batch_process_all.py imaging color lenses
```

---

## 🎯 Key Features

✅ **Universal**: Works for ANY chapter in your book
✅ **Verified**: Review agent checks all figures accounted for
✅ **Corrected**: Auto-fixes misclassifications
✅ **Cost-effective**: LLM only for uncertain cases
✅ **Educational**: Deep context understanding for 3D conversion
✅ **Interactive**: Generates production-ready Three.js visualizations
✅ **Tracked**: Comprehensive reports at each stage

---

## 📊 Expected Results

**Typical Distribution:**
- 📷 Photographs: 20-30%
- 📐 2D Diagrams: 10-20%
- 🎯 3D Candidates: 15-25%
- 📚 Composite Teaching: 10-20%
- ❓ Unknown: <10% (after review)

**3D Conversion:**
- ~3-5 figures per chapter
- Each with accurate geometry
- Interactive camera controls
- Educational annotations

---

## 🚨 Error Handling

**Missing Figures:**
```
⚠️  Missing figures: 2
   • forgotten_figure.png
   • typo_in_filename.png
🔄 Re-processing missing figure: forgotten_figure.png
✓ Added to diagrams_2d
```

**Misclassifications:**
```
⚠️  straw_camera.png: photographs → composite_teaching
✓ Moved straw_camera.png: photographs → composite_teaching
```

**Low Confidence:**
```
⚠️  Low confidence: 3 figures
🧠 LLM refining unclear cases...
✓ ambiguous.png: unknown → diagrams_3d_candidates (90%)
```

---

## 🔗 Integration Points

1. **Quarto Book**: Reads `.qmd` files, preserves figure references
2. **File System**: Organizes actual image files
3. **LLM APIs**: OpenAI GPT-4V for vision + reasoning
4. **Three.js**: Generates interactive WebGL visualizations
5. **Review Loop**: Ensures quality before conversion

No manual intervention needed - fully automated with verification!
