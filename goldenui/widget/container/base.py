from typing import Optional

from pyglet.graphics import Batch, Group
from pyglet.window import Window

from goldenui.group import ContainerGroup
from goldenui.widget.base import WidgetBase


class ContainerBase(WidgetBase):
    """The base class of all containers."""

    def __init__(
        self,
        window: Window,
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
            window (:py:class:`~pyglet.window.Window`):
                Window this container belongs to.
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
        self._window = window
        self._group = ContainerGroup(self._window, (x, y, width, height), parent=self._parent_group)
        self._widgets: list[WidgetBase] = []

    def _update_batch(self):
        for widget in self._widgets:
            widget.batch = self._batch

    def _update_group(self):
        self._group = ContainerGroup(
            (self._x, self._y, self._width, self._height), parent=self._parent_group
        )
        for widget in self._widgets:
            widget.group = self._group

    def _update_position(self):
        self._group.area = (self._x, self._y, self._width, self._height)

    def add(self, *widgets: WidgetBase):
        """Add some widgets to the container.

        Args:
            widget:
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
            widget:
                Widgets want to remove.
        """
        for widget in widgets:
            if widget in self._widgets:
                self._widgets.remove(widget)

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


__all__ = ("ContainerBase",)
