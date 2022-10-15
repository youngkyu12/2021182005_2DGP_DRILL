import game_framework
import pico2d

import main_state
Width, Height = 1280, 720
pico2d.open_canvas(Width, Height)
game_framework.run(main_state)
pico2d.close_canvas()