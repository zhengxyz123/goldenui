"""Base class of all containers.
"""

from typing import Optional, Union

from pyglet.graphics import Batch, Group
from pyglet.window import Window

from goldenui.group import ContainerGroup
from goldenui.widget.base import WidgetBase


class ContainerBase(WidgetBase):
    """The base class of all containers."""

    def __init__(
        self,
        toplevel: Union[Window, "ContainerBase"],
        x: int = 0,
        y: int = 0,
        width: int = 0,
        height: int = 0,
        *,
        enabled: bool = True,
        batch: Optional[Batch] = None,
        group: Optional[Group] = None,
    ):
        """Create a container.

        Args:
            toplevel:
                Window or container this container belongs to.
            x:
                X coordinate of the container.
            y:
                Y coordinate of the container.
            width:
                Width of the container.
            height:
                Height of the container.
            enabled:
                Whether allow user input.
            batch:
                Optional batch to add the container to.
            group:
                Optional parent group of the container.
        """
        super().__init__(x, y, width, height, enabled=enabled, batch=batch, group=group)
        if isinstance(toplevel, Window):
            self._toplevel = None
            self._window = toplevel
        else:
            self._toplevel = toplevel
            self._window = toplevel._window
        self._group = ContainerGroup(
            self._window, (x, y, width, height), parent=self._parent_group
        )
        self._widgets: list[WidgetBase] = []

    def _update_batch(self):
        for widget in self._widgets:
            widget.batch = self._batch

    def _update_group(self):
        self._group = ContainerGroup(
            self._window,
            (self._x, self._y, self._width, self._height),
            parent=self._parent_group,
        )
        self._update_position()
        for widget in self._widgets:
            widget.group = self._group

    def _update_position(self):
        if self._toplevel is None:
            self._group.area = (self._x, self._y, self._width, self._height)
        else:
            tl_area = self._toplevel._group.area
            now_x, now_y = tl_area[0] + self._x, tl_area[1] + self._y
            now_w = min(self._width, tl_area[2] - self._x)
            now_h = min(self._height, tl_area[3] - self._y)
            self._group.area = (now_x, now_y, now_w, now_h)
        for widget in self._widgets:
            widget.position = widget.position

    def add(self, *widgets: WidgetBase):
        """Add some widgets to the container.

        Args:
            widgets:
                Widgets want to add.
        """
        for widget in widgets:
            if widget not in self._widgets:
                self._widgets.append(widget)
                widget.batch = self._batch
                widget.group = self._group

    def remove(self, *widgets: WidgetBase):
        """Remove some added widgets.

        Args:
            widgets:
                Widgets want to remove.
        """
        for widget in widgets:
            if widget in self._widgets:
                self._widgets.remove(widget)

    def on_key_press(self, symbol: int, modifiers: int):
        for widget in self._widgets:
            widget.dispatch_event("on_key_press", symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int):
        for widget in self._widgets:
            widget.dispatch_event("on_key_release", symbol, modifiers)

    def on_mouse_press(self, x: int, y: int, buttons: int, modifiers: int):
        if self._check_hit(x, y) < 0:
            return
        x, y = x - self._x, y - self._y
        for widget in self._widgets:
            widget.dispatch_event("on_mouse_press", x, y, buttons, modifiers)

    def on_mouse_release(self, x: int, y: int, buttons: int, modifiers: int):
        if self._check_hit(x, y) < 0:
            return
        x, y = x - self._x, y - self._y
        for widget in self._widgets:
            widget.dispatch_event("on_mouse_release", x, y, buttons, modifiers)

    def on_mouse_drag(
        self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int
    ):
        if self._check_hit(x, y) < 0:
            return
        x, y = x - self._x, y - self._y
        for widget in self._widgets:
            widget.dispatch_event("on_mouse_drag", x, y, dx, dy, buttons, modifiers)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self._check_hit(x, y) < 0:
            return
        x, y = x - self._x, y - self._y
        for widget in self._widgets:
            widget.dispatch_event("on_mouse_motion", x, y, dx, dy)

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        if self._check_hit(x, y) < 0:
            return
        x, y = x - self._x, y - self._y
        for widget in self._widgets:
            widget.dispatch_event("on_mouse_scroll", x, y, scroll_x, scroll_y)


__all__ = ("ContainerBase",)
