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

KEY PARAMETERS:
- lab_root: Root directory of 04-Rapid-Prototyping.
- archive_dir: Target destination for historical files (experiments/).
"""

import sys
from pathlib import Path
from shutil import move as shutilMove

# -----------------------------------------------------------------------------

try:
    from microservice_toolbox.utils.bootstrap import bootstrap_microservice
except ImportError:
    for parent in Path(__file__).resolve().parents:
        toolbox_py = parent / "microservice-toolbox" / "python"
        if toolbox_py.exists():
            sys.path.insert(0, str(toolbox_py))
            break
    from microservice_toolbox.utils.bootstrap import bootstrap_microservice

bootstrap_microservice(__file__, app_name="lab_archive")

from microservice_toolbox.logger import UniLog
logger = UniLog(app_name="lab_archive", config_profile="standalone", logger_profile="devel")

# -----------------------------------------------------------------------------

def run_archive() -> None:
    lab_root = Path(__file__).resolve().parent.parent
    archive_dir = lab_root / "experiments"
    
    # 1. Ensure archive directory exists
    archive_dir.mkdir(exist_ok=True)
    
    # 2. Ensure ignore files exist
    ignore_files = [".aiignore", ".mcpignore", ".geminiignore"]
    for filename in ignore_files:
        ignore_file = archive_dir / filename
        if not ignore_file.exists():
            with open(ignore_file, "w", encoding="utf-8") as f:
                f.write("*\n")
            logger.info(f"✨ Created missing ignore file: {filename}")

    # 3. Scan for files to archive
    targets = list(lab_root.glob("CHAT-*.md")) + list(lab_root.glob("EXP-*.md"))
    
    if not targets:
        logger.info("✨ Lab is already clean: 0 files to archive.")
        return

    logger.info(f"📦 Found {len(targets)} historical file(s) to archive:")
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
        logger.info(f"  [-] Archived: {filepath.name} -> experiments/{dest.name}")

    logger.info("✅ Archiving complete: The lab root is clean and ready.")

def main():
    run_archive()

if __name__ == '__main__':
    main()
