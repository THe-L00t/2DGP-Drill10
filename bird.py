from pico2d import *

import game_world
import game_framework

PIXEL_PER_METER = (10.0/0.1)
FLY_SPEED_KMPH = 50.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM/60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

# Bird fly Speed

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x = 1600
        self.y = 400
        self.frame = 0

    def update(self):
        self.x -= 5
        self.frame = (self.frame + 1) % 14
        if self.x < -100:
            game_world.remove_object(self)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)