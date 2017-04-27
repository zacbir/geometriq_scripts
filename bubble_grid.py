import random

from geometer import *

def draw(canvas):
    canvas.set_fill_color(clear)
    g = SquareGrid(canvas.center, 128, 20, 20)
    
    for p in g.points:
        canvas.set_stroke_width(random.random() * 16)
        c = Circle(random.random() * 64 + 32)
        c.draw(canvas, at_point=p)

