from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

#rect_move

x = 0
y = 90
while (x < 790):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    x = x + 2
    delay(0.01)


while (y < 600):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    y = y + 2
    delay(0.01)

while (x >= 0):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    x = x - 2
    delay(0.01)
    
while (y >= 510):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    y = y - 2
    delay(0.01)

# circle_move

x = 1
y = 1

while (x <= 360):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(400 + (270 * math.sin(x / 360 * 2 * math.pi)), 360 - (270 * math.cos(y / 360 * 2 * math.pi)))
    y = y + 1
    x = x + 1
    delay(0.01)



close_canvas()
