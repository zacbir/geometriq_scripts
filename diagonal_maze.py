import random

from geometer import *


def draw(canvas):

    size = 128
    canvas.set_stroke_width(size / 4)

    def down_right(square:Square):
        return Line(square.points[1], square.points[3])
    
    def up_right(square:Square):
        return Line(square.points[0], square.points[2])
    
    g = SquareGrid(canvas.center, size, 25, 25)

    for p in g.points:
        s = Square(size, p)
        f = random.choice([down_right, up_right])
        f(s).draw(canvas)