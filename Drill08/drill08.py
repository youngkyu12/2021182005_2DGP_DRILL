from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
def handle_events():
    global running
    global x, y
    global dir
    global animation
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                animation = 1
                # x = x + 10
            elif event.key == SDLK_LEFT:
                animation = 0
                dir -= 1
                # x = x - 10
            elif event.key == SDLK_UP:
                dir += 2
            elif event.key == SDLK_DOWN:
                dir -= 2
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dir -= 2
            elif event.key == SDLK_DOWN:
                dir += 2




open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
animation = 0
frame = 0
dir = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * animation, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8



    if dir == 1 or dir == -1:
        x += dir * 5
    elif dir == 2:
        y += (dir - 1) * 5
    elif dir == -2:
        y += (dir + 1) * 5

    if x < 30:
        x -= dir * 5
    if x > 1280 - 30:
        x -= dir * 5
    if y > 1024 - 180:
        y -= (dir + 1) * 5
    if y < 180:
        y -= (dir - 1) * 5
    delay(0.01)

close_canvas()

