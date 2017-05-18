import random

from geometer import *

def draw(canvas):
    canvas.set_fill_color(base3)
    canvas.fill_background()
    canvas.set_stroke_color(clear)
    max_distance = 1536
    
    for c in range(10240):
        d = random.sample(range(360), 1)[0]
        shape = random.choice((WestTriangle, NorthTriangle, EastTriangle, SouthTriangle))
        fill_idx = d
        fill_skew = random.random()
        if fill_skew <= 0.25:
            fill_idx = 338 if fill_idx < 22 else fill_idx - 22
        if fill_skew >= 0.75:
            fill_idx = 22 if fill_idx > 338 else fill_idx + 22
        fill = band(fills, fill_idx, 360)        

        start = Point(random.random() * max_distance, 0)
        c = shape(96, center=start)
        canvas.set_fill_color(base03)
        c.draw(canvas, at_point=canvas.center, rotation=d)            
        canvas.set_fill_color(fill.tint())
        c.draw(canvas, at_point=canvas.center, rotation=d)

