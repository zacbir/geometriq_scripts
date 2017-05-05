import random

from geometer import *

def draw(canvas):
    g = SquareGrid(canvas.center, 400, 6, 6)
    
    c = Circle(150)
    
    for p in g.points:
        fill = band(fills, p.y, canvas.height)
        canvas.set_fill_color(fill.shade())
        canvas.set_stroke_color(fill.tint())
                
        if random.random() < 0.02:
            continue
        
        c.draw(canvas, at_point=p)

