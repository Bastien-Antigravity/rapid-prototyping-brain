#!/usr/bin/env python
# coding:utf-8

"""
🧪 LAB MANAGER (Level 04 Prototyping Sandbox utility)
Handles automated sandbox creation, repository cloning, stub extraction, and archiving.
"""
import os
import sys
import subprocess
import shutil
import json
from pathlib import Path

# --- Virtual Environment Re-Execution ---
_venv_dir = os.path.dirname(os.path.abspath(__file__))
_venv_python = os.path.join(_venv_dir, ".venv", "bin", "python3") if os.name != "nt" else os.path.join(_venv_dir, ".venv", "Scripts", "python.exe")
if os.path.exists(_venv_python) and not os.path.samefile(sys.executable, _venv_python):
    try:
        os.execl(_venv_python, _venv_python, *sys.argv)
    except OSError:
        pass

# --- Helper Functions ---

def load_inventory() -> dict:
    """Attempts to load the repository inventory from Level 05."""
    root = Path(__file__).resolve().parent
    inventory_path = root / "../05-Fleet-Operation/00-Repo-Control/inventory.json"
    if inventory_path.exists():
        try:
            with open(inventory_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Failed to parse inventory: {e}")
    return {}

def get_repo_url(repo_name_or_url: str) -> str:
    """Resolves repo name to Git URL using the fleet inventory."""
    if repo_name_or_url.startswith("http") or repo_name_or_url.startswith("git@"):
        return repo_name_or_url
        
    inventory = load_inventory()
    repos = inventory.get("repositories", [])
    for repo in repos:
        if repo.get("name") == repo_name_or_url:
            return repo.get("remote")
            
    # Fallback to Bastien-Antigravity organization URL format
    return f"https://github.com/Bastien-Antigravity/{repo_name_or_url}.git"

# --- CLI Command Operations ---

def create_sandbox(sandbox_name: str) -> Path:
    """Creates a dedicated sandbox workspace folder at the root of L04."""
    root = Path(__file__).resolve().parent
    sandbox_dir = root / sandbox_name
    
    if sandbox_dir.exists():
        print(f"ℹ️ Sandbox '{sandbox_name}' already exists.")
        return sandbox_dir
        
    print(f"🏗️ Creating isolated sandbox: {sandbox_name}...")
    (sandbox_dir / "clones").mkdir(parents=True, exist_ok=True)
    (sandbox_dir / "stubs").mkdir(parents=True, exist_ok=True)
    
    print(f"✅ Sandbox initialized at: {sandbox_dir.relative_to(root)}")
    return sandbox_dir

def clone_repo(sandbox_name: str, repo_name_or_url: str) -> None:
    """Clones a microservice repository into the sandbox folder's clones directory."""
    root = Path(__file__).resolve().parent
    sandbox_dir = root / sandbox_name
    
    if not sandbox_dir.exists():
        sandbox_dir = create_sandbox(sandbox_name)
        
    git_url = get_repo_url(repo_name_or_url)
    repo_name = repo_name_or_url.split("/")[-1].replace(".git", "")
    target_clone_dir = sandbox_dir / "clones" / repo_name
    
    if target_clone_dir.exists():
        print(f"ℹ️ Repository '{repo_name}' already cloned in sandbox.")
        return
        
    print(f"🐙 Cloning {git_url} into sandbox...")
    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", git_url, str(target_clone_dir)],
            check=True
        )
        print(f"✅ Successfully cloned '{repo_name}' into {target_clone_dir.relative_to(root)}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Git clone failed: {e}")

def extract_file(sandbox_name: str, repo_name: str, rel_file_path: str) -> None:
    """Extracts a specific file from a clone into the sandbox stubs folder."""
    root = Path(__file__).resolve().parent
    sandbox_dir = root / sandbox_name
    clone_file = sandbox_dir / "clones" / repo_name / rel_file_path
    
    if not clone_file.exists():
        print(f"❌ Error: File {rel_file_path} not found in clone '{repo_name}'.")
        return
        
    target_stub_path = sandbox_dir / "stubs" / Path(rel_file_path).name
    shutil.copy(str(clone_file), str(target_stub_path))
    print(f"📥 Extracted stub: {rel_file_path} -> {target_stub_path.relative_to(root)}")

def print_help() -> None:
    print("""🧪 Bastien-Antigravity Lab Manager
Usage:
  python lab_manager.py create <sandbox_name>
  python lab_manager.py clone <sandbox_name> <repo_name_or_url>
  python lab_manager.py extract <sandbox_name> <repo_name> <relative_file_path>
    """)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print_help()
        sys.exit(1)
        
    command = sys.argv[1]
    name = sys.argv[2]
    
    if command == "create":
        create_sandbox(name)
    elif command == "clone":
        if len(sys.argv) < 4:
            print("❌ Error: Repository name or URL is required.")
            sys.exit(1)
        clone_repo(name, sys.argv[3])
    elif command == "extract":
        if len(sys.argv) < 5:
            print("❌ Error: Repository name and file path are required.")
            sys.exit(1)
        extract_file(name, sys.argv[3], sys.argv[4])
    else:
        print(f"❌ Unknown command: {command}")
        print_help()
        sys.exit(1)
