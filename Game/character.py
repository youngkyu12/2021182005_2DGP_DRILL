from pico2d import *

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
}


class IdleState:
    def enter(character, event):
        if event == RIGHT_DOWN:
            character.velocity += 1
        elif event == LEFT_DOWN:
            character.velocity -= 1
        elif event == RIGHT_UP:
            character.velocity -= 1
        elif event == LEFT_UP:
            character.velocity += 1
        character.timer = 1000

    def exit(character, event):
        pass

    def do(character):
        character.frame = 0
        character.timer -= 1

    def draw(character):
        if character.dir == 1:
            character.image.clip_draw(character.frame * 82, 300, 82, 94, character.x, character.y)
        else:
            character.image.clip_draw(character.frame * 82, 200, 82, 94, character.x, character.y)


class RunState:
    def enter(character, event):
        if event == RIGHT_DOWN:
            character.velocity += 1
        elif event == LEFT_DOWN:
            character.velocity -= 1
        elif event == RIGHT_UP:
            character.velocity -= 1
        elif event == LEFT_UP:
            character.velocity += 1
        character.dir = character.velocity

    def exit(character, event):
        pass

    def do(character):
        character.frame = (character.frame + 1) % 5
        character.timer -= 1
        character.x += character.velocity * 5

    def draw(character):
        if character.velocity == 1:
            character.image.clip_draw(character.frame * 82, 400, 82, 94, character.x, character.y)
        else:
            character.image.clip_draw(character.frame * 82, 500, 82, 94, character.x, character.y)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
               LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState},
}

class Character:
    image = None
    def __init__(self):
        self.x, self.y = 1280 - (1026 // 2) - 128 + 41, 720 - 600 + 48
        self.frame = 0
        self.velocity = 0
        self.timer = 0
        self.dir = 1
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        if Character.image == None:
            Character.image = load_image("character_anime.png")

    def add_event(self, event):
        self.event_que.insert(0, event)
        pass

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        pass

