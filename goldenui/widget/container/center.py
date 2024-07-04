"""A container to center the widget in it.
"""

from typing import Optional

from pyglet.graphics import Batch, Group
from pyglet.window import Window

from goldenui.widget.base import WidgetBase
from goldenui.widget.container.base import ContainerBase


class CenterContainer(ContainerBase):

    def __init__(
        self,
        window: Window,
        widget: WidgetBase,
        x: int = 0,
        y: int = 0,
        width: int = 0,
        height: int = 0,
        *,
        filled: bool = False,
        enabled: bool = True,
        batch: Optional[Batch] = None,
        group: Optional[Group] = None,
    ):
        """Create a CenterContainer.

        Args:
            window (:py:class:`~pyglet.window.Window`):
                Window this container belongs to.
            widget:
                Widget that want to center.
            x:
                X coordinate of the container.
            y:
                Y coordinate of the container.
            width:
                Width of the container.
            height:
                Height of the container.
            filled:
                Whether filled the window.
            enabled:
                Whether allow user input.
            batch:
                Optional batch to add the container to.
            group:
                Optional parent group of the container.
        """
        self._filled = filled
        if self._filled:
            x, y = 0, 0
            width, height = window.width, window.height
        super().__init__(
            window, x, y, width, height, enabled=enabled, batch=batch, group=group
        )
        widget.batch = self._batch
        widget.group = self._group
        self._widgets.append(widget)

    def _update_position(self):
        if self._filled:
            self._x, self._y = 0, 0
            self._width, self._height = self._window.width, self._window.height
        super()._update_position()
        widget = self._widgets[0]
        widget.x = (self._width - widget.width) // 2
        widget.y = (self._height - widget.height) // 2

    def add(self, *widgets: WidgetBase):
        pass

    def remove(self, *widgets: WidgetBase):
        pass

    def on_resize(self, width: int, height: int):
        if not self._filled:
            return
        self.width, self.height = width, height


__all__ = ("CenterContainer",)
