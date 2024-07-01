"""Groups for internal usage.
"""

from typing import Optional

from pyglet.gl import GL_SCISSOR_TEST, glDisable, glEnable, glScissor
from pyglet.graphics import Group
from pyglet.math import Mat4, Vec3
from pyglet.window import Window


class ContainerGroup(Group):

    def __init__(
        self,
        window: Window,
        area: tuple[int],
        order: int = 0,
        parent: Optional[Group] = None,
    ):
        super().__init__(order, parent)
        self._window = window
        self._area = area
        self._prev_view = None

    @property
    def area(self) -> tuple[int]:
        return self._area

    @area.setter
    def area(self, values: tuple[int]):
        self._area = values

    def set_state(self):
        self._prev_view = self._window.view
        glEnable(GL_SCISSOR_TEST)
        glScissor(*self._area)
        self._window.view = Mat4.from_translation(Vec3(*self._area[:2], 0))

    def unset_state(self):
        pass
        self._window.view = self._prev_view
        glDisable(GL_SCISSOR_TEST)


__all__ = ("ContainerGroup",)
