from pyglet.window import Window as _Window


class GUIManager:
    def __init__(self, window: _Window):
        self._window = window


__all__ = ("GUIManager",)
