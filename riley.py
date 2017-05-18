import random

from geometer import *

def draw(canvas):
    
    canvas.set_stroke_color(clear)
    g = HorizontalHexagonGrid(canvas.center, 250, 21, 14)
    
    s = HexagonalRhombus(250)
    
    for p in g.points:
        
        canvas.set_fill_color(random.choice(fills).half())
        
        s.draw(canvas, at_point=p, rotation=240)

