from pico2d import *
import random
import game_world
import game_framework

PIXEL_PER_METER = (10.0/0.3)
FLY_SPEED_KMPH = 50.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM/60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

# Bird fly Speed

TIME_PER_ACTION = 1
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x = 1600
        self.y = random.randint(400, 550)
        self.frame = 0
        self.frame_offset_x = 0
        self.frame_offset_y = 0
        self.dir = -1

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time
        self.frame_offset_x = self.frame % 5
        self.frame_offset_y = 2 - (self.frame // 5)
        if self.x < 0 or self.x > 1600:
            self.dir *= -1

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame_offset_x) * 183,int(self.frame_offset_y) * 168 , 183, 168, self.x, self.y, 1.8*PIXEL_PER_METER, 1.6*PIXEL_PER_METER)
        else:
            self.image.clip_composite_draw(int(self.frame_offset_x) * 183,int(self.frame_offset_y) * 168 , 183, 168,0,'h', self.x, self.y, 1.8*PIXEL_PER_METER,1.6*PIXEL_PER_METER)