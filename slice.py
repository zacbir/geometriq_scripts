import random

from geometer import *

def draw(canvas):
    
    canvas.set_fill_color(canvas.stroke_color)
    
    circle = Circle(1024)

    y_margin = (canvas.height - circle.size) / 2
    x_margin = (canvas.width - circle.size) / 2
    
    circle.draw(canvas, at_point=canvas.center)
    
    starts = zip(random.sample(range(x_margin), 3), random.sample(range(y_margin, canvas.height), 3))
    
    ends = zip(random.sample(range(circle.size + x_margin, canvas.width), 3), random.sample(range(canvas.height - y_margin), 3))
    
    canvas.set_stroke_color(base03)
    
    for l in range(3):
        s_x, s_y = starts[l]
        e_x, e_y = ends[l]
        
        Line(Point(e_x, e_y), center=Point(s_x, s_y)).draw(canvas, at_point=origin)

