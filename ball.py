import math

from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0/0.3)
GRAVITY = 9.8
class Ball:
    image = None

    def __init__(self, x = 400, y = 300, thrown_speed = 15, thrown_angle = 45):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = x, y
        self.xv = thrown_speed * math.cos(math.radians(thrown_angle))
        self.yv = abs(thrown_speed*math.sin(math.radians(thrown_angle)))

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.yv -= GRAVITY * game_framework.frame_time

        self.x += self.xv *game_framework.frame_time * PIXEL_PER_METER
        self.y += self.yv *game_framework.frame_time * PIXEL_PER_METER
        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

        if self.y < 60:
            game_world.remove_object(self)