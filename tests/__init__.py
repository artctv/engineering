import pathlib
import sys


_path = pathlib.Path(__file__).parent.parent / "engineering"
sys.path.append('.')
sys.path.append(str(_path))
