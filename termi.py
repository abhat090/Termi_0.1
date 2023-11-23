import os
from random import randint

import pyglet
# Class for animating and clicking on Termi
termiGrab = "Sprites/termiGrab.gif"
termiIdle = "Sprites/termiIdle.gif"


def load_good_foodlines():
    # Take input from good food lines from ChatGPT
    inputFile = open("TermiText/goodfood.txt")
    goodLineList = []
    for line in inputFile:
        voice = line.split("\n")
        goodLineList.append(voice[0])
    return goodLineList


def output_lines(voicelines):
    randIndex = randint(0, len(voicelines) - 1)
    print(voicelines[randIndex])


def load_toy_reactions():
    # Take input from toy reactions from ChatGPT
    inputFile = open("TermiText/toy_react.txt")
    toyList = []
    for line in inputFile:
        voice = line.split("\n")
        toyList.append(voice[0])
    return toyList


# The termi_timer
def termi_timer(dt, termi, sprite, idle):
    termi.change_sprite(sprite)
    termi.idle = idle

def termi_sadness(dt, termi):
    if termi.termi_food > 5 and termi.termi_fun > 7:
        termi.termi_food -= 5
        termi.termi_fun -= 7
    if termi.termi_food < 20 and \
            termi.termi_fun < 15 and \
            not termi.termi_sad:
        termi.termi_sad = True
        termi.change_sprite("Sprites/termi-sleepy.gif")
    elif termi.termi_food > 20 and \
            termi.termi_fun > 15 and \
            termi.termi_sad:
        termi.termi_sad = False
        termi.change_sprite("Sprites/termiIdle.gif")


class Termi:
    termi_food = 50
    termi_fun = 50

    termi_sad = False

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
        if(self.termi_sad):
            print("waaa :^:")
            return
        print("meow~")
        self.change_sprite(termiGrab)
        self.idle = False
        pyglet.clock.schedule_once(termi_timer, 1.6, termi=self,
                                   sprite=termiIdle, idle=True)

    def action(self, shop_type):
        if shop_type == "terminal":
            print("Help me! </3")
            user_cmd = input(">> ")
            self.command_action(user_cmd)

        elif shop_type == "food":
            print("Buy the food DlC to feed him! - $500.99")
        elif shop_type == "play":
            print("Buy the play DLC to play with him! - $899.99")

    def command_action(self, user_cmd):
        if user_cmd == "give termi food": # or "feed termi":
            print("Yum! <3")
            if randint(0, 10) % 2 == 1:
                output_lines(load_good_foodlines())
                print("It was well worth it!! :)")
            self.termi_food += 16
        elif user_cmd == "play with termi": #or "let him PLAY":
            print("Ehehehe~ <3")
            print(output_lines(load_toy_reactions()))
            self.termi_fun += 20
        elif user_cmd == "check on termi":
            print("Food: " + str(self.termi_food) + " | Fun: " + str(self.termi_fun))
        else:
            print("That didn't do anything ;^;")

    def draw(self):
        self.sprite.draw()


