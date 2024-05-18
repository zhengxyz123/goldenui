"""gletter is a GUI framework for pyglet.
"""

import sys

__version__ = "0.0.1"

if "sphinx" in sys.modules:
    setattr(sys, "is_sphinx_run", True)
_is_sphinx_run = hasattr(sys, "is_sphinx_run") and sys.is_sphinx_run
