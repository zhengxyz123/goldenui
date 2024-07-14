"""Base class of all widgets.
"""

from typing import Any, Optional

from pyglet.event import EventDispatcher
from pyglet.graphics import Batch, Group


class WidgetBase(EventDispatcher):
    """The base class of all widgets."""

    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        width: int = 0,
        height: int = 0,
        *,
        enabled: bool = True,
        batch: Optional[Batch] = None,
        group: Optional[Group] = None,
    ):
        """Create a ``WidgetBase``.

        Args:
            x:
                X coordinate of the widget.
            y:
                Y coordinate of the widget.
            width:
                Width of the widget.
            height:
                Height of the widget.
            enabled:
                Whether allow user input.
            batch:
                Optional batch to add the widget to.
            group:
                Optional parent group of the widget.
        """
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._enabled = enabled
        self._batch = batch
        self._parent_group = group
        self._manager = None

    @property
    def x(self) -> int:
        """X coordinate of the widget."""
        return self._x

    @x.setter
    def x(self, value: int):
        self._x = value
        self._update_position()
        self.dispatch_event("on_repositioning", self)

    @property
    def y(self) -> int:
        """Y coordinate of the widget."""
        return self._y

    @y.setter
    def y(self, value: int):
        self._y = value
        self._update_position()
        self.dispatch_event("on_repositioning", self)

    @property
    def position(self) -> tuple[int, int]:
        """The ``(x, y)`` coordinate of the widget as a tuple."""
        return self._x, self._y

    @position.setter
    def position(self, values: tuple[int, int]):
        self._x, self._y = values
        self._update_position()
        self.dispatch_event("on_repositioning", self)

    @property
    def width(self) -> int:
        """Width of the widget."""
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value
        self._update_position()
        self.dispatch_event("on_repositioning", self)

    @property
    def height(self) -> int:
        """Height of the widget."""
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value
        self._update_position()
        self.dispatch_event("on_repositioning", self)

    @property
    def batch(self) -> Optional[Batch]:
        """Graphics batch."""
        return self._batch

    @batch.setter
    def batch(self, new_batch: Optional[Batch]):
        self._batch = new_batch
        self._update_batch()

    @property
    def group(self) -> Optional[Group]:
        """Parent graphics group."""
        return self._parent_group

    @group.setter
    def group(self, new_group: Optional[Group]):
        self._parent_group = new_group
        self._update_group()

    @property
    def enabled(self) -> bool:
        """Whether this widget is enabled.

        To react to changes in this value, override :py:meth:`._set_enabled` on widgets.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, new_enabled: bool):
        if self._enabled == new_enabled:
            return
        self._enabled = new_enabled
        self._set_enabled(new_enabled)

    @property
    def aabb(self) -> tuple[int, ...]:
        """Bounding box of the widget.

        Returns:
            a four-value tuple ``(x, y, x + width, y + height)``.
        """
        return self._x, self._y, self._x + self._width, self._y + self._height

    @property
    def value(self) -> Any:
        """The widget's value.

        This property allows you to set the value of a widget directly, without any user
        input. This could be used, for example, to restore widgets to a previous state,
        or if some event in your program is meant to naturally change the same value that
        the widget controls. Note that events are not dispatched when changing this
        property.
        """
        raise NotImplementedError("value depends on widget type")

    @value.setter
    def value(self, value: Any):
        raise NotImplementedError("value depends on widget type")

    def _check_hit(self, x: int, y: int) -> int:
        """Internal hook to check which part of widget has been hitted.

        Returns:
            ``-1`` means that the widget was not hitted, while other non-negative
            integers mean that different parts of the widget were hitted.
        """
        if self._x < x < self._x + self._width and self._y < y < self._y + self._height:
            return 0
        else:
            return -1

    def _set_enabled(self, enabled: bool):
        """Internal hook to set enabled.

        Override this method to perform effects when a widget is enabled or disabled.
        """
        pass

    def _update_batch(self):
        """Internal hook to change batch when :py:attr:`.batch` is modified."""
        pass

    def _update_group(self):
        """Internal hook to change group when :py:attr:`.group` is modified."""
        pass

    def _update_position(self):
        """Internal hook to change widget's position and size."""
        pass

    # Events for GoldenUI.

    def on_repositioning(self, widget: "WidgetBase"):
        pass

    # Events for pyglet.

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
        pass

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        pass

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        pass

    def on_resize(self, width: int, height: int):
        pass

    def on_text(self, text: str):
        pass

    def on_text_motion(self, motion: int):
        pass

    def on_text_motion_select(self, motion: int):
        pass


WidgetBase.register_event_type("on_key_press")
WidgetBase.register_event_type("on_key_release")
WidgetBase.register_event_type("on_mouse_press")
WidgetBase.register_event_type("on_mouse_release")
WidgetBase.register_event_type("on_mouse_drag")
WidgetBase.register_event_type("on_mouse_motion")
WidgetBase.register_event_type("on_repositioning")
WidgetBase.register_event_type("on_resize")
WidgetBase.register_event_type("on_text")
WidgetBase.register_event_type("on_text_motion")
WidgetBase.register_event_type("on_text_motion_select")


__all__ = ("WidgetBase",)
