#!/usr/bin/env python
# coding:utf-8
"""
ESSENTIAL PROCESS:
Audits the Rapid Prototyping Labs root and archives any historical CHAT or EXP files
into the 'experiments/' folder to ensure a clean, zero-friction playground.

DATA FLOW:
1. Scans the repository root for CHAT-*.md or EXP-*.md.
2. Moves found files to the 'experiments/' subdirectory.
3. Verifies that ignore files (.aiignore, .mcpignore, .geminiignore) are intact.
"""

from shutil import move as shutilMove
from pathlib import Path

def run_archive() -> None:
    root = Path(__file__).resolve().parent
    archive_dir = root / "experiments"
    
    # 1. Ensure archive directory exists
    archive_dir.mkdir(exist_ok=True)
    
    # 2. Ensure ignore files exist
    ignore_files = [".aiignore", ".mcpignore", ".geminiignore"]
    for filename in ignore_files:
        ignore_file = archive_dir / filename
        if not ignore_file.exists():
            with open(ignore_file, "w", encoding="utf-8") as f:
                f.write("*\n")
            print(f"✨ Created missing ignore file: {filename}")

    # 3. Scan for files to archive
    targets = list(root.glob("CHAT-*.md")) + list(root.glob("EXP-*.md"))
    
    if not targets:
        print("\n✨ LAB IS ALREADY PERFECTLY CLEAN & READY FOR NEW EXPERIMENTS! (0 files to archive)")
        return

    print(f"\n📦 FOUND {len(targets)} HISTORICAL FILE(S) TO ARCHIVE:")
    for filepath in targets:
        dest = archive_dir / filepath.name
        
        # Avoid overwriting in the archive if a file already exists with the same name
        if dest.exists():
            base = filepath.stem
            ext = filepath.suffix
            counter = 1
            while (archive_dir / f"{base}_{counter}{ext}").exists():
                counter += 1
            dest = archive_dir / f"{base}_{counter}{ext}"
            
        shutilMove(str(filepath), str(dest))
        print(f"  [-] Archived: {filepath.name} -> experiments/{dest.name}")

    print("\n✅ ARCHIVING COMPLETE! THE LAB ROOT IS NOW ZERO-FRICTION & READY.")

if __name__ == "__main__":
    run_archive()
