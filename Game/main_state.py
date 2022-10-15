import random
import json



from pico2d import *

import game_framework


from character import Character
from background import Background
import os

path = os.getcwd() + "\Resource"
os.chdir(path)




name = "MainState"

character = None
background = None



def enter():
    global character, background
    character = Character()
    background = Background()


def exit():
    global character, background
    del character
    del background



def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            character.handle_event(event)



def update():
    character.update()

def draw():
    clear_canvas()
    background.draw()
    character.draw()
    update_canvas()
    delay(0.05)





