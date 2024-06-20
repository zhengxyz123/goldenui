"""Manage all widgets.

In this module, :py:class:`~.GUIManager` provides a way to control widgets.
"""

from pyglet.window import Window as _Window

from goldenui.widgets.base import WidgetBase


class GUIManager:
    """A basic widgets manager, implementing a 2D spatial hash.

    It provides an efficient way to handle dispatching keyboard and mouse events to
    widgets. This is done by implementing a 2D spatial hash. Only widgets that are in the
    vicinity of the mouse pointer will be passed window events, which can greatly improve
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
        self._cells: dict[tuple[int, int], set[WidgetBase]] = {}
        self._active_widgets: set[WidgetBase] = set()
        self._mouse_pos = (0, 0)

    @property
    def enabled(self) -> bool:
        """Whether the manager is enabled."""
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

    def add(self, *widgets: WidgetBase):
        """Add some widgets to the manager.

        Args:
            widget:
                Widgets want to add.
        """
        for widget in widgets:
            min_vec = self._hash(*widget.aabb[0:2])
            max_vec = self._hash(*widget.aabb[2:4])
            for i in range(min_vec[0], max_vec[0] + 1):
                for j in range(min_vec[1], max_vec[1] + 1):
                    self._cells.setdefault((i, j), set()).add(widget)
            widget.set_handler("on_repositioning", self.on_repositioning_hook)

    def remove(self, *widgets: WidgetBase):
        """Remove some added widgets.

        Args:
            widget:
                Widgets want to remove.
        """
        for widget in widgets:
            for cell in self._cells.values():
                if widget in cell:
                    cell.remove(widget)
            widget.set_handler("on_repositioning", lambda w: None)

    def draw(self):
        """Draw all widgets in the manager."""
        pass

    def on_repositioning_hook(self, widget: WidgetBase):
        self.remove(widget, temporary=True)
        self.add(widget)

    def on_key_press(self, symbol: int, modifiers: int):
        for cell in self._cells.values():
            for widget in cell:
                widget.dispatch_event("on_key_press", symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int):
        for cell in self._cells.values():
            for widget in cell:
                widget.dispatch_event("on_key_release", symbol, modifiers)

    def on_mouse_press(self, x: int, y: int, buttons: int, modifiers: int):
        for widget in self._cells.get(self._hash(x, y), set()):
            widget.dispatch_event("on_mouse_press", x, y, buttons, modifiers)
            self._active_widgets.add(widget)

    def on_mouse_release(self, x: int, y: int, buttons: int, modifiers: int):
        for widget in self._active_widgets:
            widget.dispatch_event("on_mouse_release", x, y, buttons, modifiers)
        self._active_widgets.clear()

    def on_mouse_drag(
        self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int
    ):
        for widget in self._active_widgets:
            widget.dispatch_event("on_mouse_drag", x, y, dx, dy, buttons, modifiers)
        self._mouse_pos = x, y

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        for widget in self._cells.get(self._hash(x, y), set()):
            widget.dispatch_event("on_mouse_motion", x, y, dx, dy)
        self._mouse_pos = x, y

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        for widget in self._cells.get(self._hash(x, y), set()):
            widget.on_mouse_scroll(x, y, scroll_x, scroll_y)

    def on_text(self, text: str):
        for cell in self._cells.values():
            for widget in cell:
                widget.dispatch_event("on_text", text)

    def on_text_motion(self, motion: int):
        for cell in self._cells.values():
            for widget in cell:
                widget.dispatch_event("on_text_motion", motion)

    def on_text_motion_select(self, motion: int):
        for cell in self._cells.values():
            for widget in cell:
                widget.dispatch_event("on_text_motion_select", motion)


__all__ = ("GUIManager",)
