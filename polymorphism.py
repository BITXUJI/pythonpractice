# from ABC import abc, abstractmethod


class type1:
    def draw(self):
        print("type")


class select:
    def draw(self):
        print("select")


def draw(controls):
    for control in controls:
        control.draw()


d = type1()
s = select()
draw([d, s])
