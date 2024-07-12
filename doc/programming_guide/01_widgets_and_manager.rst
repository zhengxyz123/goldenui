Widgets and Manager
===================

Widgets are collections of elements such as buttons, sliders and input boxes that are available
for user interaction in a window. They are all inherited from
:py:class:`~pyglet.event.EventDispatcher` and :py:class:`~goldenui.widget.base.WidgetBase`. Unlike
:py:mod:`pyglet.gui`, GoldenUI provides more widgets and a default appearance.

You can get and set the position and size of a widget using the ``x``, ``y``, ``position``,
``width`` and ``height`` properties.

The ``value`` property indicates the current state of the widget, e.g. whether the button is
pressed or not. Its value has different meanings in different widgets.

Widgets are deeply bound to pyglet's event system. So it is important to understand how event
handling and dispatching work in pyglet. :ref:`handling_events` section will give you a basic
understanding.

Now let's take a look at the manager.

While widgets can be pushed to a :py:class:`~pyglet.window.Window` directly, it is not convenient
to manage them all in one place. So GoldenUI provides a :py:class:`~goldenui.manager.GUIManager` to
control all widgets, like dispatching events to some widgets and drawing them.

Create a manager is very simple::

    from pyglet.window import Window
    from goldenui.manager import GUIManager

    window = Window(...)
    manager = GUIManager(window)

A manager has following operations::

    # Add some widgets.
    manager.add(widget1, widget2, widget3, ...)
    # Remove some widgets.
    manager.remove(widget1, widget2, widget3, ...)
    # Draw all widgets.
    manager.draw()
    # Enable the manager.
    manager.enable = True
    # Disable the manager.
    manager.enable = False

The widget-manager pattern is an important design idea in GoldenUI.
