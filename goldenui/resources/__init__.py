import sys

from pyglet.image import TextureRegion
from pyglet.resource import Loader


class _ResourcesLoader:
    def __init__(self):
        if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
            path = "goldenui_res"
            self._frozen = True
        else:
            path = "@goldenui.resources"
            self._frozen = False
        self.loader = Loader(path)

    def image(self, path: str, **kwargs) -> TextureRegion:
        return self.loader.image(path, **kwargs)


loader = _ResourcesLoader()

__all__ = ("loader",)
