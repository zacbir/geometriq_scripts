from math import radians, sin, cos, sqrt
import random

from geometer import *

PHI = (1 + sqrt(5)) / 2

def draw(canvas):
    canvas.set_stroke_width(1)
    
    # x = cx + r * cos(a)
    # y = cy + r * sin(a)
    
    start_size = 3072
    
    def smaller(size, center, idx):
        if size < 64:
            return
        c = Circle(size, center=center)
        try:
            fill = fills[idx]
        except IndexError:
            fill = fills[-1]
        # fill = band(fills, size, start_size)
        canvas.set_fill_color(fill.half())
        canvas.set_stroke_color(fill)
        c.draw(canvas)
        
        angle = 64.5 * idx + 45 # random.choice(range(360))
        new_center = Point(
            center.x + size * cos(radians(angle)),
            center.y + size * sin(radians(angle))
            )
        smaller(size / PHI, new_center, idx + 1)
    
    # for s in range(3):
    smaller(start_size, Point(origin.x + 1024, origin.y), 0)

