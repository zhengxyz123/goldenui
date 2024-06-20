"""GoldenUI is a GUI library for pyglet.
"""

import sys

from pyglet import gl
from pyglet.image import Texture

__version__ = "0.0.1"

if "sphinx" in sys.modules:
    setattr(sys, "is_sphinx_run", True)
_is_sphinx_run = hasattr(sys, "is_sphinx_run") and sys.is_sphinx_run

gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)
gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
Texture.default_min_filter = gl.GL_NEAREST
Texture.default_mag_filter = gl.GL_NEAREST
