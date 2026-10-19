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
import sys
from pathlib import Path

try:
    from microservice_toolbox.utils.bootstrap import bootstrap_microservice
except ImportError:
    for parent in Path(__file__).resolve().parents:
        toolbox_py = parent / "microservice-toolbox" / "python"
        if toolbox_py.exists():
            sys.path.insert(0, str(toolbox_py))
            break
    from microservice_toolbox.utils.bootstrap import bootstrap_microservice

bootstrap_microservice(__file__, app_name="lab_manager")

from src.lab_manager import main

if __name__ == "__main__":
    main()
