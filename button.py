import pyglet
import button
from pyglet.window import mouse

batch = pyglet.graphics.Batch()

class Button:
    x = 0
    y = 0
    scale = 1
    image_name = ''

    def __init__(self, image, func, x=0, y=0, scale=1):
        self.x = x
        self.y = y
        self.scale = scale
        self.func = func

        # Load image
        self.image_name = image
        self.image = pyglet.image.load(self.image_name)
        self.sprite = pyglet.sprite.Sprite(img=self.image, batch=button.batch)

        self.sprite.scale = scale
        self.sprite.x = x
        self.sprite.y = y

        self.width = self.image.width * self.scale
        self.height = self.image.height * self.scale

    def check_over(self, x, y):
        if (
                (self.width + self.x) > x > self.x and
                (self.height + self.y) > y > self.y):
            return True
        else:
            return False

    def on_pressed(self, press_type, termi):
        termi.action(press_type)

    def draw(self):
        self.sprite.draw()
