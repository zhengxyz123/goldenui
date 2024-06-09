"""Base class of all widgets and widget styles.

In this module, gletter provides two base classes for GUI programming.

One is :py:class:`~.WidgetBase`, this class defines how a widget behaves.

The other is :py:class:`~.WidgetStyleBase`, this class defines how a widget looks like.
"""
from typing import Any, Optional, Type

from pyglet.event import EventDispatcher as _EventDispatcher
from pyglet.graphics import Batch, Group


class WidgetStyleBase:
    """The base class of all widget styles."""

    def __init__(
        self,
        widget: "WidgetBase",
        batch: Optional[Batch] = None,
        group: Optional[Group] = None,
    ):
        """
        Create a widget style.

        Args:
            widget:
                Which widget uses this style.
            batch:
                Optional batch to add the style to.
            group:
                Optional parent group of the style.
        """
        self._style_name = ""
        self._widget = widget
        self._batch = batch
        self._group = group

    @property
    def style_name(self) -> str:
        """The style name of widget."""
        return self._style_name

    @style_name.setter
    def style_name(self, new_name: str):
        if self._style_name == new_name:
            return
        self._style_name = new_name
        self._set_style()

    @property
    def batch(self) -> Batch:
        """Graphics batch."""
        return self._batch

    @batch.setter
    def batch(self, new_batch: Batch):
        self._batch = new_batch

    @property
    def group(self) -> Group:
        """Parent graphics group."""
        return self._group

    @group.setter
    def group(self, new_group: Group):
        self._group = new_group

    def _set_style(self):
        """Internal hook for setting widget style.

        Override this method to set widget style when it is changed.
        """
        pass

    def _update_position(self):
        """Internal hook for changing position and size.

        Raises:
            NotImplementedError:
                It will be occured when this method is not override.
        """
        raise NotImplementedError("unable to reposition the widget")


class WidgetBase(_EventDispatcher):
    """The base class of all widgets."""

    _style_class = WidgetStyleBase

    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        width: int = 0,
        height: int = 0,
        enabled: bool = True,
    ):
        """Create a widget.

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
        """
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._enabled = enabled
        self._focused = False
        self._style = _style_class(self)
        self._bg_group = None
        self._fg_group = None

    @property
    def x(self) -> int:
        """X coordinate of the widget."""
        return self._x

    @x.setter
    def x(self, value: int):
        self._x = value
        self._style._update_position()
        self.dispatch_event("on_repositioning", self)

    @property
    def y(self) -> int:
        """Y coordinate of the widget."""
        return self._y

    @y.setter
    def y(self, value: int):
        self._y = value
        self._style._update_position()
        self.dispatch_event("on_repositioning", self)

    @property
    def position(self) -> tuple[int, int]:
        """The ``(x, y)`` coordinate of the widget as a tuple."""
        return self._x, self._y

    @position.setter
    def position(self, values: tuple[int, int]):
        self._x, self._y = values
        self._style._update_position()
        self.dispatch_event("on_repositioning", self)

    @property
    def width(self) -> int:
        """Width of the widget."""
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value
        self._style._update_position()
        self.dispatch_event("on_repositioning", self)

    @property
    def height(self) -> int:
        """Height of the widget."""
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value
        self._style._update_position()
        self.dispatch_event("on_repositioning", self)

    @property
    def batch(self) -> Batch:
        """Graphics batch."""
        return self._style.batch

    @batch.setter
    def batch(self, new_batch: Batch):
        self._style.batch = new_batch

    @property
    def group(self) -> Group:
        """Parent graphics group."""
        return self._style.group

    @group.setter
    def group(self, new_group: Group):
        self._style.group = new_group

    @property
    def enabled(self) -> bool:
        """Whether this widget is enabled.

        To react to changes in this value, override :py:meth:`._set_enabled` on widgets.
        For example, you may want to cue the user by:

        * Playing an animation and/or sound
        * Setting a highlight color
        * Displaying a toast or notification
        """
        return self._enabled

    @enabled.setter
    def enabled(self, new_enabled: bool):
        if self._enabled == new_enabled:
            return
        self._enabled = new_enabled
        self._set_enabled(new_enabled)

    @property
    def focused(self) -> bool:
        """Whether this widget is focused.

        .. warning::
            Developer should not set this property, it will be changed by gletter itself.
            Uncorrectly focus on a widget may lead to a mess.
        """
        return self._focused

    @focused.setter
    def focused(self, new_focused: bool):
        if self._focused == new_focused:
            return
        self._focused = new_focused
        if self._focused:
            self.dispatch_event("on_focus")
        else:
            self.dispatch_event("on_unfocus")

    @property
    def aabb(self) -> tuple[int, ...]:
        """Bounding box of the widget.

        Returns:
            a four-value tuple ``(x, y, x + width, y + height)``.
        """
        return self._x, self._y, self._x + self._width, self._y + self._height

    @property
    def value(self) -> Any:
        """The Widget's value.

        This property allows you to set the value of a Widget directly, without any user
        input. This could be used, for example, to restore widgets to a previous state,
        or if some event in your program is meant to naturally change the same value that
        the widget controls. Note that events are not dispatched when changing this
        property.
        """
        raise NotImplementedError("value depends on control type")

    @value.setter
    def value(self, value: Any):
        raise NotImplementedError("value depends on control type")

    def _check_hit(self, x: int, y: int) -> int:
        """Internal hook for checking which part of widget has been hitted.

        Returns:
            ``-1`` means that the widget was not hitted, while other non-negative
            integers mean that different parts of the widget were hitted.
        """
        if self._x < x < self._x + self._width and self._y < y < self._y + self._height:
            return 0
        else:
            return -1

    def _set_enabled(self, enabled: bool):
        """Internal hook for setting enabled.

        Override this method to perform effects when a widget is enabled or disabled.
        """
        pass

    def update_groups(self, order: int):
        pass

    # Events for gletter.

    def on_focus(self):
        """Triggered when setting :py:attr:`.focused` to ``True``."""
        pass

    def on_unfocus(self):
        """Triggered when setting :py:attr:`.focused` to ``False``."""
        pass

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

    def on_text(self, text: str):
        pass

    def on_text_motion(self, motion: int):
        pass

    def on_text_motion_select(self, motion: int):
        pass


WidgetBase.register_event_type("on_focus")
WidgetBase.register_event_type("on_unfocus")
WidgetBase.register_event_type("on_repositioning")
WidgetBase.register_event_type("on_key_press")
WidgetBase.register_event_type("on_key_release")
WidgetBase.register_event_type("on_mouse_press")
WidgetBase.register_event_type("on_mouse_release")
WidgetBase.register_event_type("on_mouse_drag")
WidgetBase.register_event_type("on_mouse_motion")
WidgetBase.register_event_type("on_text")
WidgetBase.register_event_type("on_text_motion")
WidgetBase.register_event_type("on_text_motion_select")


__all__ = "WidgetBase", "WidgetStyleBase"
