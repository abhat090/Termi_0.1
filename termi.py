import os

import pyglet
import time
from pyglet.window import mouse

# Class for animating and clicking on Termi
termiGrab = "Sprites/termiGrab.gif"
termiIdle = "Sprites/termiIdle.gif"


# The termi_timer
def termi_timer(dt, termi, sprite, idle):
    termi.change_sprite(sprite)
    termi.idle = idle


class Termi:
    x = 0
    y = 0
    scale = 1
    idle = True

    def __init__(self, sprite=termiIdle, x=0, y=0, scale=1):
        self.x = x
        self.y = y
        self.scale = scale

        # Sprite Setup
        self.animation = pyglet.image.load_animation(sprite)
        self.sprite = pyglet.sprite.Sprite(img=self.animation)

        # Sprite scale and loc
        self.sprite.scale = scale
        self.sprite.x = x
        self.sprite.y = y

        self.xW = self.x + self.sprite.width - 100
        self.yH = self.y + self.sprite.height - 100

    def change_sprite(self, sprite):
        self.__init__(sprite=sprite, x=self.x, y=self.y, scale=self.scale)

    def on_pressed(self):
        print("meow~")
        self.change_sprite(termiGrab)
        self.idle = False
        pyglet.clock.schedule_once(termi_timer, 1.2, termi=self,
                                   sprite=termiIdle, idle=True)

    def draw(self):
        self.sprite.draw()


