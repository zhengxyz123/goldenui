from typing import Optional

from pyglet.graphics import Group
from pyglet import gl


class ViewportGroup(Group):
    
    def __init__(self, area: tuple[int], order: int = 0, parent: Optional[Group] = None):
        super().__init__(order, parent)
        self._area = area
    
    @property
    def area(self) -> tuple[int]:
        return self._area
    
    @area.setter
    def area(self, values: tuple[int]):
        self._area = values
    
    def set_state(self):
        pass
    
    def unset_state(self):
        pass


__all__ = ("ViewportGroup",)
