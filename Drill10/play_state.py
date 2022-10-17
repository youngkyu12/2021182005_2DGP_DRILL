from pico2d import *
import title_state
import item_state
import boy_add_delete
import game_framework
import random
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    number = 1

    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.dir = 1
        self.image = load_image('animation_sheet.png')
        self.item = None
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')


    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 2
        if self.x > 800:
            self.x = 800
            self.dir = -1
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        if self.item == 'Ball':
            self.ball_image.draw(self.x + 10, self.y + 50)
        elif self.item == 'BigBall':
            self.big_ball_image.draw(self.x + 10, self.y + 50)



grass = None
running = None
boy = None

def enter():
    global grass, running, boy
    grass = Grass()
    boy = [Boy() for i in range(Boy.number)]
    running = True

def exit():
    global boy, grass
    del boy
    del grass

def update():
    for boys in boy:
        boys.update()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def draw_world():
    grass.draw()
    for boys in boy:
        boys.draw()


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            #running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
                # game_framework.change_state(title_state)
                #running = False
            elif event.key == SDLK_i:
                game_framework.push_state((item_state))
            elif event.key == SDLK_b:
                game_framework.push_state((boy_add_delete))


    delay(0.01)

def pause():
    pass

def resume():
    pass