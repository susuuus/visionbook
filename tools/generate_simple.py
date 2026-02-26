#!/usr/bin/env python3
"""
SIMPLE DIRECT APPROACH
Just use the proven example HTML files and map to specific figures
"""

from pathlib import Path
import shutil

def main():
    """Copy proven working examples to the right figure names"""
    
    # Source templates (your proven working examples)
    pinhole_template = Path("/Users/su/Desktop/AI Augmented Book/Interactive Figures/pinhole.html")
    brdf_template = Path("/Users/su/Downloads/light_surface_3d (10).html")
    
    # Output directory
    output_dir = Path("interactive_figures/imaging")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("="*70)
    print("GENERATING 3D FIGURES - Using Proven Templates")
    print("="*70)
    print()
    
    mappings = []
    
    # 1. BRDF figure → light_surface template
    if brdf_template.exists():
        dest = output_dir / "fig-lightSpray_3d.html"
        shutil.copy(brdf_template, dest)
        mappings.append(("brdf.png", "fig-lightSpray_3d.html", "✓"))
        print(f"✓ brdf.png → {dest.name}")
    
    # 2. Wall/pinhole figure → pinhole template  
    if pinhole_template.exists():
        dest = output_dir / "fig-wallpicture_3d.html"
        shutil.copy(pinhole_template, dest)
        mappings.append(("no_picture_on_a_wall_aina.png", "fig-wallpicture_3d.html", "✓"))
        print(f"✓ no_picture_on_a_wall_aina.png → {dest.name}")
    
    # 3. Keep existing working ones
    existing = [
        "fig-pinholeGeometry_3d.html",
        "fig-pinholeGeometry2_3d.html", 
        "fig-orthographics_3d.html",
        "fig-pinhole_names_3d.html"
    ]
    
    for fname in existing:
        fpath = output_dir / fname
        if fpath.exists():
            mappings.append((fname.replace("fig-", "").replace("_3d.html", ".png"), fname, "✓"))
            print(f"✓ {fname} (already exists)")
    
    print()
    print("="*70)
    print(f"COMPLETE - {len(mappings)} visualizations ready")
    print("="*70)
    print()
    print("📁 Generated files:")
    for src, dest, status in sorted(mappings):
        print(f"  {status} {dest:<40} ← {src}")
    
    print()
    print("🌐 View at: http://localhost:8000/interactive_figures/imaging/")
    print()
    
    # List all HTML files
    all_html = sorted(output_dir.glob("*_3d.html"))
    print(f"📊 Total 3D figures: {len(all_html)}")
    for f in all_html:
        print(f"  - {f.name}")

if __name__ == '__main__':
    main()
