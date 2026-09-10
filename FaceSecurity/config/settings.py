from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

CAMERA_INDEX = 0

WINDOW_NAME = "Face Security"

FACE_DATABASE_PATH = PROJECT_ROOT / "data" / "faces.json"

FACE_MATCH_THRESHOLD = 0.6

EXIT_KEY = "q"
