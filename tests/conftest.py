import sys
from pathlib import Path

# Ensure src/ is on sys.path so imports like
# `from src.python_ci_pavedroad_template_app.app import app` work when
# running pytest from the repository root or when VS Code runs test discovery.
root = Path(__file__).resolve().parents[1]
src_dir = str(root / "src")
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)
