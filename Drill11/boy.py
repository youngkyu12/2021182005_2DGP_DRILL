from pico2d import *

#2. 이벤트 정의
# RD, LD, RU, LU = 0, 1, 2, 3
RD, LD, RU, LU, TIMER, AD = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): AD
}




class IDLE:
    def enter(self, event):    # 상태에 들어갈 때 행하는 액션
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000
        pass

    def exit(self, event):     # 상태를 나올 때 행하는 액션, 고개 들기
        print('EXIT IDLE')
        pass

    def do(self):       # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)
        pass

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

        pass

class RUN:
    @staticmethod
    def enter(self, event):
        print('ENTER RUN')
        # 방향을 결정해야 하는데, 뭘 근거로? 어떤 키가 눌렸기 때문에?
        # 키 이벤트 정보가 필요.
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        pass

    @staticmethod
    def exit(self, event):
        print('EXIT RUN')
        if event == AD:
            if self.dir == -1:
                self.face_dir = -1
            elif self.dir == 1:
                self.face_dir = 1
        else:
            self.face_dir = self.dir

        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        # x 좌표 변경, 달리기
        self.x += self.dir
        self.x = clamp(0, self.x, 800) # 특정 범위로 값을 제한하는 함수
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

        pass

class SLEEP:
    def enter(self, event):    # 상태에 들어갈 때 행하는 액션
        print('ENTER IDLE')
        self.frame = 0
        pass

    def exit(self, event):     # 상태를 나올 때 행하는 액션, 고개 들기
        print('EXIT IDLE')
        pass

    def do(self):       # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + 1) % 8
        pass

    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           -3.141592 / 2, '',
                                           self.x + 25, self.y - 25, 100, 100)
        else: # 오른쪽
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           3.141592 / 2, '',
                                           self.x + 25, self.y - 25, 100, 100)

        pass

class AUTO_RUN:
    def enter(self, event):    # 상태에 들어갈 때 행하는 액션
        print('ENTER IDLE')
        if self.face_dir == 1:
            self.dir = 1
        elif self.face_dir == -1:
            self.dir = -1
        pass

    def exit(self, event):     # 상태를 나올 때 행하는 액션, 고개 들기
        print('EXIT IDLE')
        if self.dir == 1:
            self.face_dir = 1
        if self.dir == -1:
            self.face_dir = -1
        else:
            self.dir = 0
        pass

    def do(self):       # 상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + 1) % 8
        # x 좌표 변경, 달리기
        self.x += self.dir
        if 800 < self.x:
            self.dir = -1
        elif 0 > self.x:
            self.dir = 1
        pass

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

        pass


#3. 상태 변환 깃ㄹ
next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AD: AUTO_RUN},     # 동시입력을 위해 RU, LU가 있어야 된다.
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, AD: AUTO_RUN},   # 동시입력을 위해 RD, LD가 있어야 된다.
    SLEEP: {RD: RUN, LD: RUN, RU: RUN, LU: RUN, AD: SLEEP},
    AUTO_RUN: {RD: RUN, LD: RUN, RU: RUN, LU: RUN, AD: IDLE}
}



class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []     # 이벤트 큐 초기화
        self.cur_state = IDLE
        self.cur_state.enter(self, None)  # 초기 상태의 entry 액션 수행


    def update(self):
        self.cur_state.do(self)     # 현재 상태의 do 액션 수행.

        # 이벤트를 확인해서, 이벤트가 있으면 이벤트 변환 처리
        if self.q:  # 큐에 이벤트가 있으면, 이벤트가 발생했으면,
            event = self.q.pop()
            self.cur_state.exit(self, event)   # 현재 상태를 나가야되고,
            self.cur_state = next_state[self.cur_state][event]    # 다음 상태를 구한다.
            self.cur_state.enter(self, event)  # 다음 상태의 entry action 수행

        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)

        # if self.dir == -1:
        #     self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        # elif self.dir == 1:
        #     self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        # else:
        #     if self.face_dir == 1:
        #         self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #     else:
        #         self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1