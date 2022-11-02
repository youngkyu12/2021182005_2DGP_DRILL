# class Star:     # 클래스의 역할: 함수, 또는 변수를 묶는다. 그룹이름으로(그룹핑)
#     x = 100
#     def change():
#         x = 200
#         print('x is', x)
#
# print(Star.x)   # Star zmffotm x 는 클래스 변수
# Star.change()   # 클래스 함수 호출
#
# star = Star()
# star.change()

class Player:
    def __init__(self):
        self.x = 100
    def where(self):
        print(self.x)

player = Player()
player.where()

# Player.where()
Player.where(player)
player.where()  # 객체 함수 호출 == Player.where(player)