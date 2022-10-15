from pico2d import *
import os

path = os.getcwd() + "\Resource"
os.chdir(path)

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600
class Background:
    def __init__(self):
        self.background = load_image('Background_finalexam_1024x600.png')
        self.hart = load_image('Hart.png')
        self.font = load_font('ENCR10B.TTF', 21)
        self.ItemBox = load_image('ItemBox.png')

    def draw(self):
        self.hart.draw(21, 720 - 21)
        self.hart.draw(21 + 42 + 1, 720 - 21)
        self.hart.draw(64 + 42 + 1, 720 - 21)
        self.background.draw(Width // 2, bg_Height // 2 + 120)
        self.font.draw(1280 - 128, 720 - 10, "Target:", (0, 0, 0))
        self.font.draw(1280 - 1024 - 130, 720 - 600 - 10 - 16, "Item", (0, 0, 0))
        self.ItemBox.draw(1280 - 1024 - 130 + 90, 720 - 600 - 32)

class Enmey:
    def __init__(self):
        self.Bug = load_image("Bug_Enemy.png")
        # self.soju = load_image()

class Character:
    def __init__(self):
        self.x, self.y = 1280 - 1026 - 128 + 41, 720 - 600 + 48
        self.frame = 0
        self.character = load_image("Move_Right.png")

    def update(self):
        self.frame = (self.frame + 1) % 9
        delay(0.1)
        self.x += 5

    def draw(self):
        self.character.clip_draw(self.frame * 82, 0, 82, 96, self.x, self.y)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()

Back = None
character = None
running = None

def enter():
    global Back, running, character
    Back = Background()
    character = Character()
    running = True

def exit():
    global Back, running, character
    del Back
    del character
    running = False

def update():
    character.update()

def draw():
    clear_canvas()
    Back.draw()
    character.draw()
    update_canvas()

open_canvas(Width, Height)
hide_lattice()
enter()

while running:
    handle_events()
    draw()
    update()
exit()

close_canvas()