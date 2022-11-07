# objects[0] : 바닥계층
# objects[1] : 상위계층
objects = [[], [], []]


def add_object(o, depth):
    objects[depth].append(o)

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            del o
            return
    raise ValueError('Trying destroy non existing object')
    # objects.remove(o)   # 리스트에서 삭제
    # del o   # 메모리에서 삭제

def all_abjects():
    for layer in objects:
        for o in layer:
            yield o     # 제너레이터, 모든 객체들을 하나씩 넘겨준다.

def clear():
    for o in all_abjects():
        del o
    for layer in objects:
        layer.clear()