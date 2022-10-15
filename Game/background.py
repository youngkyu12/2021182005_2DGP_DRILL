from pico2d import *
import os

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

class Background:
    background = None
    hart = None
    font = None
    ItemBox = None
    def __init__(self):     # 호출할 때마다 생성하게됨 조건문을 통해 단 한번의 이미지 로딩만 수행
        if Background.background == None:
            self.background = load_image('Background_finalexam_1024x600.png')
        if Background.hart == None:
            self.hart = load_image('Hart.png')
        if Background.font == None:
            self.font = load_font('ENCR10B.TTF', 21)
        if Background.ItemBox == None:
            self.ItemBox = load_image('ItemBox.png')

    def draw(self):
        self.hart.draw(21, 720 - 21)
        self.hart.draw(21 + 42 + 1, 720 - 21)
        self.hart.draw(64 + 42 + 1, 720 - 21)
        self.background.draw(Width // 2, bg_Height // 2 + 120)
        self.font.draw(1280 - 128, 720 - 10, "Target:", (0, 0, 0))
        self.font.draw(1280 - 1024 - 130, 720 - 600 - 10 - 16, "Item", (0, 0, 0))
        self.ItemBox.draw(1280 - 1024 - 130 + 90, 720 - 600 - 32)