from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024



open_canvas(KPU_WIDTH,KPU_HEIGHT)

# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')
running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
#hide_cursor()
hand_arrow_x, hand_arrow_y = random.randint(1, KPU_WIDTH), random.randint(1, KPU_HEIGHT)

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    hand_arrow.draw(hand_arrow_x, hand_arrow_y)

    if x <= hand_arrow_x and y <= hand_arrow_y:
        x += 1
        y += 1
    elif x >= hand_arrow_x and y <= hand_arrow_y:
        x -= 1
        y += 1
    elif x <= hand_arrow_x and y >= hand_arrow_y:
        x += 1
        y -= 1
    else:
        x -= 1
        y -= 1

    if x == hand_arrow_x and y == hand_arrow_y:
        hand_arrow_x, hand_arrow_y = random.randint(1, KPU_WIDTH), random.randint(1, KPU_HEIGHT)

    delay(0.01)
    update_canvas()

    frame = (frame + 1) % 8








