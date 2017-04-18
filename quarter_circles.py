import random
from geometer import *

def draw(canvas):
    canvas.set_fill_color(clear)
    g = SquareGrid(canvas.center, 512, 8, 8)
    g2 = SquareGrid(Point(canvas.center.x + g.size / 2, canvas.center.y + g.size / 2), 512, 9, 9)
    
    for p in g.points:
        stroke = random.choice(warms)
        a = QuarterCircle(248)
        for t in range(4):
            canvas.set_stroke_color(stroke.shade())
            canvas.set_stroke_width(16)
            a.draw(canvas, at_point=p, rotation=t * 90)

    for p in g2.points:
        a = QuarterCircle(248)
        stroke = random.choice(warms)
        for t in range(4):
            canvas.set_stroke_color(stroke.shade())
            canvas.set_stroke_width(16)
            a.draw(canvas, at_point=p, rotation=t * 90)
