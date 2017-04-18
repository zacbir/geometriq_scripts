import random

from geometer import *

def draw(canvas):
    
    canvas.set_stroke_color(base1)
    canvas.set_fill_color(base03)
    canvas.fill_background()

    t = Triangle(400)    

    grid = HorizontalHexagonGrid(canvas.center, 200, 12, 4)
    
    for p in grid.points:
        fill = random.choice((base02, base01, green))
        canvas.set_stroke_width(random.random() * 5 + 0.5)
        canvas.set_fill_color(base03)
        t.draw(canvas, at_point=p)
        canvas.set_fill_color(fill.shade())
        t.draw(canvas, at_point=p)

