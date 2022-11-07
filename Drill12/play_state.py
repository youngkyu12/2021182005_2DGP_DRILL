from pico2d import *
import game_framework
import game_world

from grass_back import Grass_Back
from grass_front import Grass_Front
from boy import Boy


boy = None  # boy의 event를 전달하기 위해 남겨둔다.
grass_back = None
ball = None
grass_front = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)


# 초기화
def enter():
    global boy, grass_back, grass_front
    boy = Boy()
    grass_back = Grass_Back()
    grass_front = Grass_Front()
    game_world.add_object(boy, 1)
    game_world.add_object(grass_back, 0)
    game_world.add_object(grass_front, 2)

# 종료
def exit():
    game_world.clear()
    # global boy, grass
    # del boy
    # del grass
    pass

def update():
    for game_object in game_world.all_abjects():
        game_object.update()
    # for layer in game_world.objects:
    #     for game_object in layer:
    #         game_object.update()
    # for game_object in game_world.objects:
    #     game_object.update()
    # boy.update()
    # ball.update()


def draw_world():
    for game_object in game_world.all_abjects():
        game_object.draw()
    # for layer in game_world.objects:
    #     for game_object in layer:
    #         game_object.draw()
    # for game_object in game_world.objects:
    #     game_object.draw()
    # grass.draw()
    # boy.draw()
    # ball.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
