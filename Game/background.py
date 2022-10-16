from pico2d import *
import os

Width, Height = 1280, 720
bg_Width, bg_Height = 1024, 600

class Background:
    background = None
    hart = None
    font = None
    ItemBox = None
    gauge = None
    mailbox = None
    def __init__(self):     # 호출할 때마다 생성하게됨 조건문을 통해 단 한번의 이미지 로딩만 수행
        if Background.background == None:
            self.background = load_image('Background_finalexam_1024x600.png')
        if Background.hart == None:
            self.hart = load_image('Hart.png')
        if Background.font == None:
            self.font = load_font('ENCR10B.TTF', 23)
        if Background.ItemBox == None:
            self.ItemBox = load_image('ItemBox_32x32.png')
        if Background.gauge == None:
            self.gauge = load_image('gauge.png')
        if Background.mailbox == None:
            self.mailbox = load_image('mail.png')

    def draw(self):
        self.hart.draw(21, 720 - 21)
        self.hart.draw(21 + 42 + 1, 720 - 21)
        self.hart.draw(64 + 42 + 1, 720 - 21)
        self.background.draw(Width // 2, bg_Height // 2 + 120)
        self.font.draw(1280 - 128, 720 - 10, "Target:", (0, 0, 0))
        self.font.draw(1280 - 1024 - 130, 720 - 600 - 10, "Item", (0, 0, 0))
        self.ItemBox.draw(1280 - 1024 - 130 + 76, 720 - 600 - 16)
        self.gauge.draw(1280 - 130 - 63, 720 - 600 - 16)
        self.ItemBox.draw(1280 - 130 - 128 - 20, 720 - 600 - 16)
        self.mailbox.draw(64, 720 - 600 + 64)
        self.mailbox.draw(1280 - 130 + 64, 720 - 600 + 64)
