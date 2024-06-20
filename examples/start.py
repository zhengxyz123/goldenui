from random import randint

from pyglet import app, clock
from pyglet.window import Window

from goldenui.manager import GUIManager
from goldenui.widgets import TextButton

window = Window(400, 300, "Example")
manager = GUIManager(window)
button = TextButton("Hello", 125, 120, 150, 60, font_size=20)
manager.add(button)


@window.event
def on_draw():
    window.clear()
    manager.draw()


@button.event
def on_click():
    x, y = randint(0, 250), randint(0, 240)
    button.position = x, y


if __name__ == "__main__":
    clock.schedule_interval(window.draw, 1 / 60)
    app.run()
