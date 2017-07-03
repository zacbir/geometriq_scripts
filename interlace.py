import random

from geometer import *

def draw(canvas):
    
    size = 30
    canvas.set_stroke_width(30)
    g = HorizontalHexagonGrid(canvas.center, size, 60, 20)
    
    for p in g.points:
        
        canvas.set_stroke_color(random.choice(fills).shade())
        l = Line(Point(size, 0), center=origin)
        l.draw(canvas, at_point=p)

