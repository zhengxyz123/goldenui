"""Some useful functions and classes.
"""


class space:
    """The size of the empty area around the widget.

    Used for ``margin`` and ``padding`` parameters.
    """

    def __init__(self, *value: int):
        """Create a ``space`` object.

        Args:
            value:
                A tuple with 1 to 4 non-negative elements.

        - When 1 value is specified, it applies the same space to all four sides.
        - When 2 values are specified, the first value applies to the top and bottom, the
          second to the left and right.
        - When 3 values are specified, the first value applies to the top, the second to
          the left and right, the third to the bottom.
        - When 4 values are specified, the values apply to the top, right, bottom, and
          left in that order (clockwise).

        Raises:
            ValueError:
                Raised when passing negative integers or when passing 0 or 5 and more
                parameters.
        """
        if not all(map(lambda x: x >= 0, value)):
            raise ValueError("parameters must be non-negative values")
        if len(value) == 1:
            self._top, self._bottom = value[0], value[0]
            self._left, self._right = value[0], value[0]
        elif len(value) == 2:
            self._top, self._bottom = value[0], value[0]
            self._left, self._right = value[1], value[1]
        elif len(value) == 3:
            self._top = value[0]
            self._left, self._right = value[1], value[1]
            self._bottom = value[2]
        elif len(value) == 4:
            self._top, self._right, self._bottom, self._left = value
        else:
            raise ValueError(f"expect 1 to 4 value(s), but {len(value)} are given")

    def __repr__(self) -> str:
        return f"space({self._top}, {self._right}, {self._bottom}, {self._left})"

    @property
    def left(self) -> int:
        return self._left

    @property
    def right(self) -> int:
        return self._right

    @property
    def top(self) -> int:
        return self._top

    @property
    def bottom(self) -> int:
        return self._bottom


__all__ = ("space",)
