import os
import zipfile
from pathlib import Path

BASE_DIR = Path(r"C:\Users\mohamad.abdelraouf\.gemini\antigravity\scratch\cybershield-ai")
ZIP_PATH = BASE_DIR / "CyberShield-AI-GitHub-Ready.zip"

EXCLUDE_DIRS = {"__pycache__", ".git", ".venv", "env", ".idea", ".vscode"}
EXCLUDE_FILES = {"cloudflared.exe", "CyberShield-AI-GitHub-Ready.zip"}

with zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            if file in EXCLUDE_FILES or file.endswith(('.pyc', '.db-wal', '.db-shm')):
                continue
            full_path = Path(root) / file
            arc_name = full_path.relative_to(BASE_DIR)
            zipf.write(full_path, arc_name)

print(f"✅ Created ZIP file: {ZIP_PATH} ({os.path.getsize(ZIP_PATH) / (1024*1024):.2f} MB)")
