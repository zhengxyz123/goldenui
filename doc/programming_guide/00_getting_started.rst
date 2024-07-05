Getting Started
===============

Install the Library
-------------------

.. note:: This library is not uploaded to PyPI now.

GoldenUI can be downloaded and installed by ``pip``:

.. code:: sh

    pip install goldenui

Alternatively, you can clone the source code from GitHub and install it manually:

.. code:: sh

    git clone git@github.com:zhengxyz123@goldenui.git
    cd goldenui
    pip install .

Write a Simple Application
--------------------------

In this section, we are going to create a simple program which has one button. After reading the
following, you will have a rough idea of the architecture of GoldenUI.

A GoldenUI application is also a pyglet application. So we assume that you know something about
pyglet and OpenGL.

First, import every needed module::

    from random import randint

    from pyglet import app, clock, gl
    from pyglet.image import Texture
    from pyglet.window import Window

    from goldenui.manager import GUIManager
    from goldenui.widgets import TextButton

After that, we need to set up OpenGL since GoldenUI uses pixel style widgets::

    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
    Texture.default_min_filter = gl.GL_NEAREST
    Texture.default_mag_filter = gl.GL_NEAREST

Then, create a :py:class:`~pyglet.window.Window` and a :py:class:`~goldenui.manager.GUIManager`::

    window = Window(400, 300, "Getting Started")
    manager = GUIManager(window)

And create a :py:class:`~goldenui.widget.button.TextButton` located at center of the window
with text "Hello" of size 20::

    button = TextButton("Hello", 110, 120, 180, 60, font_size=20)

The ``button`` must be added to ``manager`` in order to work::

    manager.add(button)

After button has been pressed, the :py:attr:`~goldenui.widget.button.TextButton.on_click` event
is triggered. We can override this event to move the button randomly::

    @button.event
    def on_click():
        x, y = randint(0, 220), randint(0, 240)
        button.position = x, y

Don't forget to draw widgets::

    @window.event
    def on_draw():
        window.clear()
        manager.draw()

Finally, run the program::

    if __name__ == "__main__":
        clock.schedule_interval(window.draw, 1 / 60)
        app.run()
