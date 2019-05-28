import random

from geometer import *


def draw(canvas):

    size = 128
    canvas.set_stroke_width(size / 4)

    def left(square:Square):
        return Line(square.points[0], square.points[1])

    def top(square:Square):
        return Line(square.points[1], square.points[2])

    def right(square:Square):
        return Line(square.points[2], square.points[3])

    def bottom(square:Square):
        return Line(square.points[3], square.points[0])
    
    g = SquareGrid(canvas.center, size, 25, 25)

    for p in g.points:
        s = Square(size, p)
        [func(s).draw(canvas) for func in random.sample([left, top, right, bottom], random.choice([1, 1, 2]))]