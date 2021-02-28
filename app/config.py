import json
from pathlib import Path

CLEAR_LINE = "\033[K"

SPINNERS_DICT = json.loads((Path.cwd() / "app" / "assets" / "spinners.json").read_text())["spinners"]
