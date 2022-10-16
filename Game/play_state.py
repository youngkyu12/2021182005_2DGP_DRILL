from pico2d import *
import os

path = os.getcwd() + "\Resource"
os.chdir(path)

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
}

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600
class Background:
    background = None
    hart = None
    font = None
    ItemBox = None
    def __init__(self):     # 호출할 때마다 생성하게됨 조건문을 통해 단 한번의 이미지 로딩만 수행
        if Background.background == None:
            self.background = load_image('Background_finalexam_1024x600.png')
        if Background.hart == None:
            self.hart = load_image('Hart.png')
        if Background.font == None:
            self.font = load_font('ENCR10B.TTF', 21)
        if Background.ItemBox == None:
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
    image = None
    def __init__(self):
        self.x, self.y = 1280 - (1026 // 2) - 128 + 41, 720 - 600 + 48
        self.frame = 0
        self.animation = 1
        self.dir = 0
        self.events = None
        if Character.image == None:
            Character.image = load_image("character_anime.png")

    def update(self):
        self.events = get_events()
        self.x += self.dir * 5
        if self.animation == 3 or self.animation == 2:
            self.frame = (self.frame + 1) % 5

    def draw(self):
        Character.image.clip_draw(self.frame * 82, self.animation * 96, 82, 96, self.x, self.y)

    def key_events(self):
        for event in self.events:
            if event.type == SDL_KEYDOWN:
                print("keydown")
                if event.key == SDLK_LEFT:
                    print("keydown_left")
                    self.dir = -1
                    self.animation = 3
                elif event.key == SDLK_RIGHT:
                    print("keydown_right")
                    self.dir = 1
                    self.animation = 2

        self.dir = 0
        if self.animation == 3:
            self.animation = 0
        elif self.animation == 2:
            self.animation = 1
        delay(0.05)

def exit_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()

# def key_events(dir, frame, animation):
#     events = get_events()
#     for event in events:
#         if event.type == SDL_KEYDOWN:
#             print("keydown")
#             if event.key == SDLK_LEFT:
#                 print("keydown_left")
#                 dir = -1
#                 animation = 3
#             elif event.key == SDLK_RIGHT:
#                 print("keydown_right")
#                 dir = 1
#                 animation = 2
#         elif event.type == SDL_KEYUP:
#             print("keyup")
#             dir = 0
#             if animation == 3:
#                 animation = 0
#             elif animation == 2:
#                 animation = 1
#         delay(0.05)
#     return dir, frame, animation

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
    character.key_events()


def draw():
    clear_canvas()
    Back.draw()
    character.draw()
    update_canvas()

open_canvas(Width, Height)
hide_lattice()
enter()

while running:
    exit_events()
    update()
    draw()
exit()
