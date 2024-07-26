from pyglet import app, clock, gl
from pyglet.image import Texture
from pyglet.window import Window

from goldenui.manager import GUIManager
from goldenui.widget import CenterContainer, TextButton

gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)
gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
Texture.default_min_filter = gl.GL_NEAREST
Texture.default_mag_filter = gl.GL_NEAREST

window = Window(400, 300, "Example - CenterContainer", resizable=True)
window.set_minimum_size(400, 300)
manager = GUIManager(window)
button = TextButton("Hello", width=180, height=60, font_size=20)
container = CenterContainer(window, button, filled=True)
manager.add(container)


@window.event
def on_draw():
    window.clear()
    manager.draw()


if __name__ == "__main__":
    clock.schedule_interval(window.draw, 1 / 60)
    app.run()
