#!/usr/bin/env python
# coding:utf-8

"""
ESSENTIAL PROCESS:
Bootstrap entrypoint wrapper for lab_manager.py. Re-executes under virtual environment and delegates command execution to src/lab_manager.py.

DATA FLOW:
1. Re-executes in .venv if available.
2. Adds src/ to sys.path.
3. Imports and runs main from lab_manager.
"""
import os
import sys
from pathlib import Path

# --- Virtual Environment Re-Execution Ritual ---
_self_dir = Path(__file__).resolve().parent
_venv_python = _self_dir / ".venv" / "Scripts" / "python.exe" if os.name == "nt" else _self_dir / ".venv" / "bin" / "python3"
if os.path.exists(_venv_python):
    try:
        if not os.path.samefile(sys.executable, _venv_python):
            os.execl(_venv_python, _venv_python, *sys.argv)
    except OSError:
        pass

# Add src to system path
_src_dir = _self_dir / "src"
if str(_src_dir) not in sys.path:
    sys.path.insert(0, str(_src_dir))

from lab_manager import main

if __name__ == "__main__":
    main()
