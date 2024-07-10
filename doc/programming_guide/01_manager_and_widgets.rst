Manager and Widgets
===================

While widgets can be pushed to a :py:class:`~pyglet.window.Window` directly, it is not convenient
to manage them all in one place. So GoldenUI provides a :py:class:`~goldenui.manager.GUIManager` to
control all widgets, like dispatching events to some widgets and drawing them.

Create a manager is very simple::

    from pyglet.window import Window
    from goldenui.manager import GUIManager

    window = Window(...)
    manager = GUIManager(window)

It also has an optional parameter called ``cell_size`` which is for internal use only and changing
its value is not recommended.

A manager has following operations::

    # Add some widgets.
    manager.add(widget1, widget2, widget3, ...)
    # Remove some widgets.
    manager.remove(widget1, widget2, widget3, ...)
    # Enable the manager.
    manager.enable = True
    # Disable the manager.
    manager.enable = False
