from typing import Optional

from pyglet import gl
from pyglet.graphics import Group
from pyglet.image import get_buffer_manager


class ViewportGroup(Group):

    def __init__(
        self, area: tuple[int], order: int = 0, parent: Optional[Group] = None
    ):
        super().__init__(order, parent)
        self._area = area
        self._prev_area = None

    @property
    def area(self) -> tuple[int]:
        return self._area

    @area.setter
    def area(self, values: tuple[int]):
        self._area = values

    def set_state(self):
        self._prev_area = get_buffer_manager().get_viewport()
        gl.glViewport(*self._area)

    def unset_state(self):
        gl.glViewport(*self._prev_area)


__all__ = ("ViewportGroup",)
