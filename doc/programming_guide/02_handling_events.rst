.. _handling_events:

Handling Events
===============

There is nothing extra in this section, just additional notes on `Event Dispatching & Handling
<https://pyglet.readthedocs.io/en/latest/programming_guide/events.html>`_ and
:py:mod:`pyglet.event` in pyglet documentation. But please also read the following carefully.

First, do not set up event handlers for pyglet-specific events such as
:py:attr:`~pyglet.window.Window.on_mouse_press` and
:py:attr:`~pyglet.window.Window.on_mouse_release`. This is because widgets can usually handle these
events and may conflict with user-set handlers. For example, if you want to handle the event of a
click on a :py:class:`~goldenui.widget.button.TextButton`, it is most appropriate to handle the
:py:attr:`~goldenui.widget.button.TextButton.on_click` event provided by the widget.

Second, mouse events are triggered when the mouse button is clicked, the mouse is moved, or the
mouse wheel is rolled, **not** when the cursor is inside the widget. If you want to know if the
cursor is inside the widget, you should use the
:py:meth:`~goldenui.widget.base.WidgetBase._check_hit` method.
