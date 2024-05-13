"""ThreePatch and NinePatch.

Patchs are like :py:class:`pyglet.sprite.Sprite`, but they split a whole image into
several parts to avoid distortion when scaling them.
"""

from typing import Optional

from pyglet.graphics import Batch, Group
from pyglet.image import AbstractImage
from pyglet.sprite import Sprite


class ThreePatch:
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        left: AbstractImage,
        middle: AbstractImage,
        right: AbstractImage,
        batch: Optional[Batch] = None,
        group: Optional[Group] = None,
    ):
        """Create a ThreePatch.

        Args:
            x:
                X coordinate of the ThreePatch.
            y:
                Y coordinate of the ThreePatch.
            width:
                The desire width of ThreePatch.
            height:
                The desire height of ThreePatch.
            left:
                The left part.
            middle:
                The middle part.
            right:
                The right part.
            batch:
                Optional batch to add the patch to.
            group:
                Optional parent group of the patch.
        """
        self._x, self._y = x, y
        self._width = width
        self._height = height
        self._sprites = []
        self._sprites.append(Sprite(left, batch=batch, group=group))
        self._sprites.append(Sprite(middle, batch=batch, group=group))
        self._sprites.append(Sprite(right, batch=batch, group=group))
        self._update()

    def __getitem__(self, key: int | slice) -> Sprite | tuple[Sprite, ...]:
        if isinstance(key, int):
            return self._sprites[key]
        elif isinstance(key, slice):
            return self._sprites[key]
        else:
            raise ValueError("unsupported operation")

    def __setitem__(self, key: int, value: AbstractImage | tuple[AbstractImage, ...]):
        if isinstance(key, int) and isinstance(value, AbstractImage):
            self._sprites[key].image = value
        elif isinstance(key, slice):
            for i in [0, 1, 2][key]:
                self._sprites[i].image = value[i]
        else:
            raise ValueError("unsupported operation")
        self._update()

    @property
    def x(self) -> int:
        """X coordinate of the ThreePatch."""
        return self._x

    @x.setter
    def x(self, x: int):
        self._x = x
        self._update()

    @property
    def y(self) -> int:
        """Y coordinate of the ThreePatch."""
        return self._y

    @y.setter
    def y(self, y: int):
        self._y = y
        self._update()

    @property
    def position(self) -> tuple[int, int]:
        """The (x, y) coordinates of the patch, as a tuple."""
        return self._x, self._y

    @position.setter
    def position(self, position: tuple[int, int]):
        self._x, self._y = position
        self._update()

    @property
    def width(self) -> int:
        """The desire width of ThreePatch."""
        return self._width

    @width.setter
    def width(self, width: int):
        self._width = width
        self._update()

    @property
    def height(self) -> int:
        """The desire height of ThreePatch."""
        return self._height

    @height.setter
    def height(self, height: int):
        self._height = height
        self._update()

    @property
    def batch(self) -> Batch:
        """Graphics batch."""
        return self._sprites[0].batch

    @batch.setter
    def batch(self, batch: Batch):
        for sprite in self._sprites:
            sprite.batch = batch

    @property
    def group(self) -> Group:
        """Parent graphics group."""
        return self._sprites[0].group

    @group.setter
    def group(self, group: Group):
        for sprite in self._sprites:
            sprite.group = group

    def _update(self):
        corner_width = self._sprites[0].image.width
        corner_height = self._sprites[0].image.height
        corner_width *= self._height / corner_height

        self._sprites[0].scale = self._height / corner_height
        self._sprites[2].scale = self._height / corner_height
        self._sprites[1].width = self._width - 2 * corner_width
        self._sprites[1].height = self._height

        self._sprites[0].position = (self._x, self._y, 0)
        self._sprites[1].position = (self._x + corner_width, self._y, 0)
        self._sprites[2].position = (self._x + self._width - corner_width, self._y, 0)

    def draw(self):
        """Draw the patch at its current position.

        Using this method is not recommended, please see pyglet's documentation for more
        information.
        """
        for sprite in self._sprites:
            sprite.draw()

    def update(
        self,
        *,
        x: Optional[int] = None,
        y: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
    ):
        """Simultaneously change the position and size.
        
        Args:
            x:
                X coordinate of the ThreePatch.
            y:
                Y coordinate of the ThreePatch.
            width:
                The desire width of ThreePatch.
            height:
                The desire height of ThreePatch.
        """
        if x is not None:
            self._x = x
        if y is not None:
            self._y = y
        if width is not None:
            self._width = width
        if height is not None:
            self._height = height
        self._update()


class NinePatch:
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        # fmt: off
        tl: AbstractImage, tm: AbstractImage, tr: AbstractImage,
        ml: AbstractImage, mm: AbstractImage, mr: AbstractImage,
        bl: AbstractImage, bm: AbstractImage, br: AbstractImage,
        # fmt: on
        batch: Optional[Batch] = None,
        group: Optional[Group] = None,
    ):
        """Create a NinePatch.

        Args:
            x:
                X coordinate of the NinePatch.
            y:
                Y coordinate of the NinePatch.
            width:
                The desire width of NinePatch.
            height:
                The desire height of NinePatch.
            tl:
                The top-left corner.
            tm:
                The top-middle part.
            tr:
                The top-right corner.
            ml:
                The middle-left part.
            mm:
                The central part.
            mr:
                The middle-right part.
            bl:
                The bottom-left corner.
            bm:
                The bottom-middle part.
            br:
                The bottom-right corner.
            batch:
                Optional batch to add the patch to.
            group:
                Optional parent group of the patch.
        """
        # The `scale` property doesn't scale all sprites, it just scales
        # tl, tr, bl and br sprites.
        self._scale = 1
        self._x, self._y = x, y
        self._width = width
        self._height = height
        self._sprites = {}
        self._sprites[(0, 0)] = Sprite(tl, batch=batch, group=group)
        self._sprites[(0, 1)] = Sprite(tm, batch=batch, group=group)
        self._sprites[(0, 2)] = Sprite(tr, batch=batch, group=group)
        self._sprites[(1, 0)] = Sprite(ml, batch=batch, group=group)
        self._sprites[(1, 1)] = Sprite(mm, batch=batch, group=group)
        self._sprites[(1, 2)] = Sprite(mr, batch=batch, group=group)
        self._sprites[(2, 0)] = Sprite(bl, batch=batch, group=group)
        self._sprites[(2, 1)] = Sprite(bm, batch=batch, group=group)
        self._sprites[(2, 2)] = Sprite(br, batch=batch, group=group)
        self._update()

    def __getitem__(self, key: tuple[int, ...]) -> Sprite:
        return self._sprites[key]

    @property
    def scale(self) -> float:
        """Scale the corner sprites."""
        return self._scale

    @scale.setter
    def scale(self, scale: float):
        self._scale = scale
        self._update()

    @property
    def x(self) -> int:
        """X coordinate of the ThreePatch."""
        return self._x

    @x.setter
    def x(self, x: int):
        self._x = x
        self._update()

    @property
    def y(self) -> int:
        """Y coordinate of the ThreePatch."""
        return self._y

    @y.setter
    def y(self, y: int):
        self._y = y
        self._update()

    @property
    def position(self) -> tuple[int, int]:
        """The (x, y) coordinates of the patch, as a tuple."""
        return self._x, self._y

    @position.setter
    def position(self, position: tuple[int, int]):
        self._x, self._y = position
        self._update()

    @property
    def width(self) -> int:
        """The desire width of ThreePatch."""
        return self._width

    @width.setter
    def width(self, width: int):
        self._width = width
        self._update()

    @property
    def height(self) -> int:
        """The desire height of ThreePatch."""
        return self._height

    @height.setter
    def height(self, height: int):
        self._height = height
        self._update()

    @property
    def batch(self) -> Batch:
        """Graphics batch."""
        return self._sprites[(0, 0)].batch

    @batch.setter
    def batch(self, batch: Batch):
        for sprite in self._sprites.values():
            sprite.batch = batch

    @property
    def group(self) -> Group:
        """Parent graphics group."""
        return self._sprites[(0, 0)].group

    @group.setter
    def group(self, group: Group):
        for sprite in self._sprites.values():
            sprite.group = group

    def _update(self):
        for coord in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            self._sprites[coord].scale = self._scale

        top_width = self._sprites[(0, 0)].width
        top_height = self._sprites[(0, 0)].height
        bottom_width = self._sprites[(2, 0)].width
        bottom_height = self._sprites[(2, 0)].height
        middle_width = self._width - 2 * top_width
        middle_height = self._height - top_height - bottom_height

        self._sprites[(0, 1)].width = self._sprites[(2, 1)].width = middle_width
        self._sprites[(0, 1)].height = top_height
        self._sprites[(2, 1)].height = bottom_height

        self._sprites[(1, 0)].width = self._sprites[(1, 2)].width = top_width
        self._sprites[(1, 0)].height = self._sprites[(1, 2)].height = middle_height
        self._sprites[(1, 1)].width = middle_width
        self._sprites[(1, 1)].height = middle_height

        self._sprites[(2, 0)].position = (self._x, self._y, 0)
        self._sprites[(2, 1)].position = (self._x + bottom_width, self._y, 0)
        self._sprites[(2, 2)].position = (
            self._x + bottom_width + middle_width,
            self._y,
            0,
        )
        self._sprites[(1, 0)].position = (self._x, self._y + bottom_height, 0)
        self._sprites[(1, 1)].position = (
            self._x + bottom_width,
            self._y + bottom_height,
            0,
        )
        self._sprites[(1, 2)].position = (
            self._x + bottom_width + middle_width,
            self._y + bottom_height,
            0,
        )
        self._sprites[(0, 0)].position = (
            self._x,
            self._y + bottom_height + middle_height,
            0,
        )
        self._sprites[(0, 1)].position = (
            self._x + top_width,
            self._y + bottom_height + middle_height,
            0,
        )
        self._sprites[(0, 2)].position = (
            self._x + top_width + middle_width,
            self._y + bottom_height + middle_height,
            0,
        )

    def draw(self):
        """Draw the patch at its current position.

        Using this method is not recommended, please see pyglet's documentation for more
        information.
        """
        for sprite in self._sprites.values():
            sprite.draw()

    def update(
        self,
        *,
        x: Optional[int] = None,
        y: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
    ):
        """Simultaneously change the position and size.
        
        Args:
            x:
                X coordinate of the NinePatch.
            y:
                Y coordinate of the NinePatch.
            width:
                The desire width of NinePatch.
            height:
                The desire height of NinePatch.
        """
        if x is not None:
            self._x = x
        if y is not None:
            self._y = y
        if width is not None:
            self._width = width
        if height is not None:
            self._height = height
        self._update()


__all__ = "ThreePatch", "NinePatch"
