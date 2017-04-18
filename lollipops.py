import random

from geometer import *

def draw(canvas):

    background, stroke = base03, base1
    
    canvas.set_stroke_color(stroke)
    canvas.set_fill_color(background)
    canvas.fill_background()

    points = []
        
    for i in range(32):
        p = Point(random.random() * canvas.width,
        random.random() * canvas.height)
        
        points.append(p)
        
        l = Line(to_point=p, center=canvas.center())
        l.draw(canvas, at_point=origin, rotation=0)
    
    for p in points:
        c = Circle(random.random() * 256)
        c.draw(canvas, at_point=p, rotation=0)
