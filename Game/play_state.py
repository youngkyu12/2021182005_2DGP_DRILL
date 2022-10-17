from pico2d import *
import game_framework
import os

path = os.getcwd() + "\Resource"
os.chdir(path)

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600
class Background:
    background = None
    hart = None
    font_item = None
    font_score = None
    ItemBox = None
    def __init__(self):     # 호출할 때마다 생성하게됨 조건문을 통해 단 한번의 이미지 로딩만 수행
        if Background.background == None:
            self.background = load_image('Background_finalexam_1024x600.png')
        if Background.hart == None:
            self.hart = load_image('Hart.png')
        if Background.font_item == None:
            self.font_item = load_font('ENCR10B.TTF', 21)
        if Background.font_score == None:
            self.font_score = load_font('ENCR10B.TTF', 15)
        if Background.ItemBox == None:
            self.ItemBox = load_image('ItemBox.png')

    def draw(self):
        self.hart.draw(21, 720 - 21)
        self.hart.draw(21 + 42 + 1, 720 - 21)
        self.hart.draw(64 + 42 + 1, 720 - 21)
        self.background.draw(Width // 2, bg_Height // 2 + 120)
        self.font_score.draw(1280 - 130, 720 - 10, "TargetScore", (0, 0, 0))
        self.font_score.draw(1280 - 130, 720 - 40, "MyScore", (0, 0, 0))
        self.font_item.draw(1280 - 1024 - 130, 720 - 600 - 10 - 16, "Item", (0, 0, 0))
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
        self.dir_x = 0
        self.dir_y = 0
        if Character.image == None:
            Character.image = load_image("character_anime.png")

    def update(self):
        self.x += self.dir_x * 2
        self.y += self.dir_y * 2
        if self.animation == 4 or self.animation == 5:
            self.frame = (self.frame + 1) % 5
        else:
            self.frame = 0
        if self.y > 720 - 600 + 48 + 100:
            self.dir_y -= 1
        elif self.y < 720 - 600 + 48:
            self.dir_y = 0
            if character.animation == 0:
                character.animation = 5
            elif character.animation == 1:
                character.animation = 4


    def draw(self):
        Character.image.clip_draw(self.frame * 82, self.animation * 100, 82, 96, self.x, self.y)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                close_canvas()
            elif event.key == SDLK_LEFT:
                character.dir_x -= 1
                character.animation = 5
            elif event.key == SDLK_RIGHT:
                character.dir_x += 1
                character.animation = 4
            elif event.key == SDLK_UP:
                if character.animation == 5 or character.animation == 2:
                    character.animation = 0
                elif character.animation == 4 or character.animation == 3:
                    character.animation = 1
                character.dir_y += 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                character.dir_x += 1
                character.animation = 2
            elif event.key == SDLK_RIGHT:
                character.dir_x -= 1
                character.animation = 3


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
    update()
    draw()
exit()
