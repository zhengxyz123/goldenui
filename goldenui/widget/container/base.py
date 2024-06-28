from goldenui.widget.base import WidgetBase


class ContainerBase(WidgetBase):
    """The base class of all container."""

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
        """Create a container.

        Args:
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


__all__ = ("ContainerBase",)
