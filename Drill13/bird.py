from pico2d import *
import game_framework
import game_world
import random

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0   # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class Bird:
    image = None
    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x = random.randint(50, 1500)
        self.y = random.randint(300, 500)
        self.dir = 1
        self.frame = 0
        self.animation = 2
    def draw(self):
        if self.dir == 1:
            Bird.image.clip_draw(int(self.frame)*182, self.animation * 168, 182, 168, self.x, self.y)
        elif self.dir == -1:
            Bird.image.clip_composite_draw(int(self.frame) * 182, self.animation * 168, 182, 168,
                                           3.141592 / 180, 'h', self.x, self.y, 168, 182)

    def update(self):
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        if self.frame > 5:
            self.animation = (self.animation + 1) % 3
        if self.x < 50 or self.x > 1600 - 50:
            self.dir *= -1
