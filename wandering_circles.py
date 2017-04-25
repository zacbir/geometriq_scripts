from math import sqrt
import random

from geometer import *

def draw(canvas):
    # canvas.set_stroke_color(base1.hair())
    start = canvas.center
    
    diag = sqrt((canvas.width / 2)**2 + (canvas.height / 2)**2)
    
    size = diag
    
    while size > 1:
        fill = band(list(reversed(fills)), size, diag)
        # opacity = size / diag
        canvas.set_stroke_width(random.random() * 10)
        canvas.set_stroke_color(base1.shade())
        canvas.set_fill_color(fill.hair())
        c = Circle(size, center=start)
        
        c.draw(canvas)
        
        d_x = (random.random() * (size / 4) - size / 8) + start.x
        d_y = (random.random() * (size / 4) - size / 8) + start.y
         
        start = Point(d_x, d_y)

        size = (1 - random.random() * 0.1) * size

