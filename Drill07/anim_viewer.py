from pico2d import *

open_canvas()

character = load_image('sprite_sheet.png')

action_all = 7  # 총 액션 개수
frame = 0   # 현재 프레임 번호
frame_all = 6   # 총 프레임 개수

def animation(action):
    global frame
    global action_all
    global frame_all
    for frame in range(0, frame_all):
        clear_canvas()
        character.clip_draw(frame * (582 // frame_all), (497 // action_all) * action, 582 // frame_all, 497 //
                            action_all, 800 // 2, 600 // 2)
        update_canvas()
        frame = frame % frame_all
        delay(0.05)
        get_events()

while True:
    for action in range(action_all, 0, -1):
        animation(action)
    break

close_canvas()
