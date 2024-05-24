"""Manage all widgets.

In this module, :py:class:`~.GUIManager` provides a way to control widgets.
"""

from typing import Iterable

from pyglet.window import Window as _Window

from gletter.widgets.base import WidgetBase


class GUIManager:
    """A basic widgets manager, implementing a 2D spatial hash.

    It provides an efficient way to handle dispatching keyboard and mouse events to
    widgets. This is done by implementing a 2D spatial hash. Only widgets that are in the
    vicinity of the mouse pointer will be passed Window events, which can greatly improve
    efficiency when a large quantity of widgets are in use.
    """

    def __init__(self, window: _Window, cell_size: int = 256):
        """Create a GUIManager.

        Args:
            window (:py:class:`~pyglet.window.Window`):
                Manager will receive events from this window and these events will be
                passed on to every added widgets.
            cell_size:
                Size of the spatial hash.
        """
        self._window = window
        self._enabled = True
        self._cell_size = cell_size
        self._cells = {}
        self._active_widgets = set()
        self._mouse_pos = (0, 0)

    @property
    def enabled(self) -> bool:
        """Get and set whether the manager is enabled."""
        return self._enabled

    @enabled.setter
    def enabled(self, new_enabled: bool):
        if self._enabled == new_enabled:
            return
        self._enabled = new_enabled
        if self._enabled:
            self._window.push_handlers(self)
            self._mouse_pos = self._window._mouse_x, self._window._mouse_y
            self.on_mouse_motion(*self._mouse_pos, 0, 0)
        else:
            self._window.remove_handlers(self)

    def _hash(self, x: int, y: int) -> tuple[int, int]:
        """Normalize position to cell."""
        return x // self._cell_size, y // self._cell_size

    def add(self, widget: Iterable[WidgetBase] | WidgetBase):
        """Add some widgets to the manager.

        Args:
            widget:
                Widgets want to add.
        """
        pass

    def remove(
        self, widget: Iterable[WidgetBase] | WidgetBase, temporary: bool = False
    ):
        """Remove some added widgets.

        Args:
            widget:
                Widgets want to remove.
            temporary:
                Remove widgets temporarily so that it can be added more quickly.

        .. warning::
            The ``temporary`` parameter is for internal usage. Developer should not turn
            it on.
        """
        pass

    def draw(self):
        """Draw all widgets in the manager."""
        pass

    def on_repositioning_hook(self, widget: WidgetBase):
        self.remove(widget, temporary=True)
        self.add(widget)

    def on_key_press(self, symbol: int, modifiers: int):
        pass

    def on_key_release(self, symbol: int, modifiers: int):
        pass

    def on_mouse_press(self, x: int, y: int, buttons: int, modifiers: int):
        pass

    def on_mouse_release(self, x: int, y: int, buttons: int, modifiers: int):
        pass

    def on_mouse_drag(
        self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int
    ):
        self._mouse_pos = x, y

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self._mouse_pos = x, y

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        pass

    def on_text(self, text: str):
        pass

    def on_text_motion(self, motion: int):
        pass

    def on_text_motion_select(self, motion: int):
        pass


__all__ = ("GUIManager",)
