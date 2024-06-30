from pyglet import app, clock, gl
from pyglet.image import Texture
from pyglet.window import Window

from goldenui.manager import GUIManager
from goldenui.widget.container.base import ContainerBase
from goldenui.widget import TextButton

gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)
gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
Texture.default_min_filter = gl.GL_NEAREST
Texture.default_mag_filter = gl.GL_NEAREST

window = Window(400, 300, "Example", resizable=True)
manager = GUIManager(window)
container = ContainerBase(200, 150, 200, 150)
button1 = TextButton("Hello", 5, 5, 180, 60, font_size=20)
button2 = TextButton("Hello", 5, 5, 180, 60, font_size=20)
container.add(button1)
manager.add(container, button2)


@window.event
def on_draw():
    window.clear()
    manager.draw()

@window.event
def on_resize(width, height):
    container.position = width // 2, height // 2
    container.width = width // 2
    container.height = height // 2


if __name__ == "__main__":
    clock.schedule_interval(window.draw, 1 / 60)
    app.run()
