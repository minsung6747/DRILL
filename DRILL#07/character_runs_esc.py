from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas()
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')
kpu_ground = load_image('KPU_GROUND.png')
running = True
x = 0
frame = 0
hand_arrow_x = random.random()
hand_arrow_y = random.random()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    cursor.draw()
    update_canvas()







