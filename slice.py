import random

from geometer import *

def draw(canvas):
    canvas.set_fill_color(base1)
    canvas.set_stroke_color(base1)
    
    circle = Circle(1024)

    y_margin = (canvas.height - circle.size * 2) / 2
    x_margin = (canvas.width - circle.size * 2) / 2
    
    circle.draw(canvas, at_point=canvas.center)

    lines = 3

    starts = zip(random.sample(range(x_margin), lines), random.sample(range(y_margin, canvas.height), lines))
    
    ends = zip(random.sample(range(circle.size * 2 + x_margin, canvas.width), lines), random.sample(range(canvas.height - y_margin), lines))
    
    canvas.set_stroke_color(base03)
    
    for l in range(lines):
        s_x, s_y = starts[l]
        e_x, e_y = ends[l]
        
        Line(Point(e_x, e_y), center=Point(s_x, s_y)).draw(canvas, at_point=origin)

