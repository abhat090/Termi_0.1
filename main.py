import pyglet
import termi
import button
from random import randint

from pyglet.window import mouse
from pyglet.gl import *

# Setup main window
window_height: int = 300
window_width: int = 250

window = pyglet.window.Window(window_width, window_height,
                              caption="Termi.py",
                              visible=False)

pyglet.gl.glClearColor(0.2, 0.4, 0.5, 1)

# initialize window
window.set_visible()

# Items in main window
# Termi himself!
myTermi = termi.Termi(scale=10,
                      x=-80, y=-100)

# Terminal Button
buttonTerminal = button.Button(image="Sprites/termi-nal.png", func="smth",
                               scale=0.5,
                               x=200, y=10)

buttonFood = button.Button(image="Sprites/termi-food.png", func="food",
                           scale=1,
                           x=25, y=180)

buttonPlay = button.Button(image="Sprites/termi-toy.png", func="play",
                           scale=1,
                           x=145, y=180)

pyglet.clock.schedule_interval(termi.termi_sadness, 10.0, myTermi)
@window.event
def on_mouse_press(x, y, click, modifiers):
    if click == mouse.LEFT:
        if (myTermi.xW > x > myTermi.x and myTermi.yH > y > myTermi.y) and myTermi.idle:
            myTermi.on_pressed()
        elif buttonTerminal.check_over(x,y):
            buttonTerminal.on_pressed("terminal", myTermi)
        elif buttonPlay.check_over(x,y):
            buttonPlay.on_pressed("play", myTermi)
        elif buttonFood.check_over(x,y):
            buttonFood.on_pressed("food", myTermi)


@window.event
def on_draw():
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    window.clear()

    button.batch.draw()
    myTermi.draw()

pyglet.app.run()
