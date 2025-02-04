from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = BASE_DIR.parent
PROJECT_DIR = BACKEND_DIR.parent
APPS_DIR = BACKEND_DIR / "apps"
