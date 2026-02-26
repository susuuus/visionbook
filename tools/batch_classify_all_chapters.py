#!/usr/bin/env python3
"""
Process chapters one at a time with review between each
"""

import subprocess
import sys
from pathlib import Path
import json


def get_chapters():
    """Get list of chapters with figures"""
    chapters = []
    for qmd_file in Path('.').glob('*.qmd'):
        chapter_name = qmd_file.stem
        # Skip slides and special files
        if '_slides' not in chapter_name and chapter_name not in ['index', 'references', 'notations']:
            # Check if figures folder exists
            fig_folder = Path(f'figures/{chapter_name}')
            if fig_folder.exists():
                chapters.append(chapter_name)
    return sorted(chapters)


def process_chapter(chapter: str) -> dict:
    """Process single chapter"""
    print(f"\n{'='*70}")
    print(f"🎨 PROCESSING: {chapter}")
    print(f"{'='*70}")
    
    try:
        result = subprocess.run(
            ['.venv/bin/python', 'tools/complete_figure_pipeline.py', chapter],
            timeout=300
        )
        
        if result.returncode == 0:
            # Load report
            report_path = Path(f'figures_sorted/{chapter}/classification_report.json')
            if report_path.exists():
                with open(report_path) as f:
                    return json.load(f)
        return None
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def show_summary(report: dict):
    """Show chapter summary"""
    print(f"\n{'─'*70}")
    print("📊 RESULTS")
    print(f"{'─'*70}")
    
    for cat, count in report['summary'].items():
        if count > 0:
            print(f"  {cat}: {count}")
    
    if report.get('3d_conversion_ready'):
        print(f"\n🎯 3D candidates: {len(report['3d_conversion_ready'])}")
        for fig in report['3d_conversion_ready']:
            print(f"     • {fig}")
    
    print(f"\n🔍 Review status: {'✅ Verified' if not report['review']['issues_found'] else '⚠️ Issues found'}")


def main():
    import os
    
    # Check API key
    if not os.getenv('OPENAI_API_KEY'):
        print("⚠️  WARNING: OPENAI_API_KEY not set")
        print("   LLM review will be disabled")
        print("   Set with: export OPENAI_API_KEY='sk-...'")
        print()
    
    chapters = get_chapters()
    
    print("="*70)
    print("📚 CHAPTER-BY-CHAPTER PROCESSING")
    print("="*70)
    print(f"Found {len(chapters)} chapters with figures")
    print()
    
    # Show chapters
    for i, ch in enumerate(chapters, 1):
        print(f"  {i}. {ch}")
    
    print("\nThis will process ONE chapter at a time.")
    print("You can review results before continuing.\n")
    
    response = input("Start processing? (y/n): ")
    if response.lower() != 'y':
        print("Aborted.")
        return
    
    results = {
        'processed': [],
        'skipped': []
    }
    
    for i, chapter in enumerate(chapters, 1):
        print(f"\n{'='*70}")
        print(f"[{i}/{len(chapters)}] Chapter: {chapter}")
        print(f"{'='*70}")
        
        # Process
        report = process_chapter(chapter)
        
        if report and report['total_figures'] > 0:
            show_summary(report)
            results['processed'].append({
                'chapter': chapter,
                'total': report['total_figures'],
                '3d_candidates': len(report.get('3d_conversion_ready', []))
            })
            
            # Ask to continue
            if i < len(chapters):
                print(f"\n{'─'*70}")
                response = input(f"Continue to next chapter ({chapters[i]})? (y/n/q to quit): ")
                if response.lower() == 'q':
                    print("\nStopping. You can resume later.")
                    break
                elif response.lower() != 'y':
                    print(f"Skipping remaining chapters.")
                    results['skipped'].extend(chapters[i:])
                    break
        else:
            print(f"⚠️  No figures found in {chapter}")
    
    # Final summary
    print(f"\n{'='*70}")
    print("📊 FINAL SUMMARY")
    print(f"{'='*70}")
    print(f"Processed: {len(results['processed'])} chapters")
    
    total_figs = sum(r['total'] for r in results['processed'])
    total_3d = sum(r['3d_candidates'] for r in results['processed'])
    
    print(f"Total figures: {total_figs}")
    print(f"Total 3D candidates: {total_3d}")
    
    if results['processed']:
        print(f"\n✅ Processed chapters:")
        for r in results['processed']:
            print(f"   • {r['chapter']}: {r['total']} figures ({r['3d_candidates']} 3D)")
    
    print("\n✅ Chapter-by-chapter processing complete!")


if __name__ == '__main__':
    main()

