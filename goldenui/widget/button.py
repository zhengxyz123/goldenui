"""Some useful buttons.

In this submodule, GoldenUI defines several buttons.

:py:class:`TextButton` is a button that shows one line of text.
"""

from typing import Optional

from pyglet.graphics import Batch, Group
from pyglet.text import Label
from pyglet.window import mouse

from goldenui import is_sphinx_run
from goldenui.patch import ThreePatch
from goldenui.resources import loader
from goldenui.widget.base import WidgetBase

text_color_white = (255, 255, 255, 255)
text_color_gray = (170, 170, 170, 255)
text_button_image = {
    "normal": [],
    "hover": [],
    "pressed": [],
}
for status in ["normal", "hover", "pressed"]:
    for part in ["left", "middle", "right"]:
        # Without the `if` statement, sphinx will raise a warning when building doc.
        if not is_sphinx_run:
            text_button_image[status].append(
                loader.image(f"buttons/{status}_{part}.png")
            )


class TextButton(WidgetBase):
    """A button with text."""

    def __init__(
        self,
        text: str,
        x: int = 0,
        y: int = 0,
        width: int = 0,
        height: int = 0,
        *,
        enabled: bool = True,
        font_name: Optional[list[str] | str] = None,
        font_size: Optional[int] = None,
        batch: Optional[Batch] = None,
        group: Optional[Group] = None,
    ):
        """Create a TextButton.

        Args:
            x:
                X coordinate of the button.
            y:
                Y coordinate of the button.
            width:
                Width of the button.
            height:
                Height of the button.
            enabled:
                Whether allow user interact.
            font_name:
                Font family name(s) for text.
            font_size:
                Font size for text.
            batch:
                Optional batch to add the button to.
            group:
                Optional parent group of the button.
        """
        super().__init__(x, y, width, height, enabled=enabled, batch=batch, group=group)
        self._button_group = Group(order=0, parent=group)
        self._label_group = Group(order=1, parent=group)
        self._button = ThreePatch(
            self._x,
            self._y,
            self._width,
            self._height,
            *text_button_image["normal"],
            batch=batch,
            group=self._button_group,
        )
        self._label = Label(
            text,
            x=self._x + self._width // 2,
            y=self._y + self._height // 2,
            color=text_color_white,
            anchor_x="center",
            anchor_y="center",
            align="center",
            font_name=font_name,
            font_size=font_size,
            batch=batch,
            group=self._label_group,
        )
        self._pressed = False
        self._set_enabled(enabled)

    @property
    def text(self) -> str:
        """Text on the button."""
        return self._label.text

    @text.setter
    def text(self, text: str):
        self._label.text = text

    @property
    def value(self) -> bool:
        """Whether user is clicked the button."""
        return self._pressed
    
    @value.setter
    def value(self, new_value: bool):
        pass

    def _set_enabled(self, enabled: bool):
        if enabled:
            self._button[:] = text_button_image["normal"]
            self._label.color = text_color_white
        else:
            self._button[:] = text_button_image["pressed"]
            self._label.color = text_color_gray

    def _update_batch(self):
        self._button.batch = self._batch
        self._label.batch = self._batch

    def _update_group(self):
        self._button_group = Group(order=0, parent=self._parent_group)
        self._label_group = Group(order=1, parent=self._parent_group)
        self._button.group = self._button_group
        self._label.group = self._label_group

    def _update_position(self):
        self._button.update(
            x=self._x, y=self._y, width=self._width, height=self._height
        )
        self._label.position = (
            self._x + self._width // 2,
            self._y + self._height // 2,
            0,
        )

    def on_mouse_press(self, x: int, y: int, buttons: int, modifiers: int):
        if (
            not self._enabled
            or not self._check_hit(x, y) >= 0
            or not buttons & mouse.LEFT
        ):
            return
        self._button[:] = text_button_image["pressed"]
        self._pressed = True

    def on_mouse_release(self, x: int, y: int, buttons: int, modifiers: int):
        if not self._enabled or not self._pressed:
            return
        self._label.color = (
            text_color_gray if self._check_hit(x, y) >= 0 else text_color_white
        )
        status = "hover" if self._check_hit(x, y) >= 0 else "normal"
        self._button[:] = text_button_image[status]
        self._pressed = False
        self.dispatch_event("on_click")

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if not self._enabled or self._pressed:
            return
        self._label.color = (
            text_color_gray if self._check_hit(x, y) >= 0 else text_color_white
        )
        status = "hover" if self._check_hit(x, y) >= 0 else "normal"
        self._button[:] = text_button_image[status]

    def on_mouse_drag(
        self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int
    ):
        if not self._enabled or self._pressed:
            return
        self._label.color = (
            text_color_gray if self._check_hit(x, y) >= 0 else text_color_white
        )
        status = "hover" if self._check_hit(x, y) >= 0 else "normal"
        self._button[:] = text_button_image[status]

    if is_sphinx_run:

        def on_click(self):
            """This event will be triggered when release the mouse."""
            pass


TextButton.register_event_type("on_click")


__all__ = ("TextButton",)
