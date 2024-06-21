"""GoldenUI is a GUI library for pyglet.
"""

import sys
from dataclasses import dataclass

#: The release version.
version = "0.0.1"
__version__ = version

is_sphinx_run = False
if "sphinx" in sys.modules:
    is_sphinx_run = True
