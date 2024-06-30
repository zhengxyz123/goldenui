goldenui.widget.base
====================

.. automodule:: goldenui.widget.base

.. autoclass:: WidgetBase
    :show-inheritance:

    .. rubric:: Properties
    .. autoproperty:: x
    .. autoproperty:: y
    .. autoproperty:: position
    .. autoproperty:: width
    .. autoproperty:: height
    .. autoproperty:: batch
    .. autoproperty:: group
    .. autoproperty:: enabled
    .. autoproperty:: aabb
    .. autoproperty:: value

    .. rubric:: Internal Hooks
    .. automethod:: _check_hit
    .. automethod:: _set_enabled
    .. automethod:: _update_batch
    .. automethod:: _update_group
    .. automethod:: _update_position

    .. rubric:: Events

    The following events are triggered by pyglet, they are described in
    :py:mod:`pyglet.window` thoroughly.

    .. automethod:: on_key_press
    .. automethod:: on_key_release
    .. automethod:: on_mouse_press
    .. automethod:: on_mouse_release
    .. automethod:: on_mouse_drag
    .. automethod:: on_mouse_motion
    .. automethod:: on_mouse_scroll
    .. automethod:: on_text
    .. automethod:: on_text_motion
    .. automethod:: on_text_motion_select

    .. rubric:: Special Methods
