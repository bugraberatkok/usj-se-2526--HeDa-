import sys
from pathlib import Path

# project root = folder that contains "src" and "tests"
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))
