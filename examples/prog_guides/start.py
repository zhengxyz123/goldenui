from random import randint

from pyglet import app, clock, gl
from pyglet.image import Texture
from pyglet.window import Window

from goldenui.manager import GUIManager
from goldenui.widget import TextButton

gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)
gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
Texture.default_min_filter = gl.GL_NEAREST
Texture.default_mag_filter = gl.GL_NEAREST

window = Window(400, 300, "Example - Getting Started")
manager = GUIManager(window)
button = TextButton("Hello", 110, 120, 180, 60, font_size=20)
manager.add(button)


@window.event
def on_draw():
    window.clear()
    manager.draw()


@button.event
def on_click():
    x, y = randint(0, 220), randint(0, 240)
    button.position = x, y


if __name__ == "__main__":
    clock.schedule_interval(window.draw, 1 / 60)
    app.run()
