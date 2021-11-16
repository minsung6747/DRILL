import random
from pico2d import *
import game_world
import game_framework


PIXEL_PER_METER = (10.0 / 1)  # 10 pixel 100 cm
RUN_SPEED_KMPH = 2.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed         초당 2회의 액션
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.x, self.y  = random.randint(0, 800), 500
        self.frame = 0

    def do(self):
        self.frame=(self.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 14
        self.x += RUN_SPEED_PPS * game_framework.frame_time



    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        # fill here for draw

    def update(self):


        self.x += RUN_SPEED_PPS
        self.frame = (self.frame + 1) % 14


