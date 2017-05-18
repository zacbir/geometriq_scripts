import random

from geometer import *

def draw(canvas):
    #canvas.set_stroke_width(1)
    canvas.set_stroke_color(clear)
    canvas.set_fill_color(base1)
    
    angle = random.random() * 90
    
    h = HalfCircle(256, center=Point(-1024, 0))
    h.draw(canvas, at_point=canvas.center, rotation=180 + angle)
    
    canvas.set_stroke_color(base1)
    canvas.set_fill_color(clear)
    
    for x in range(512):
        
        radius = 768 + x
        start_angle = random.random() * 60
        
        a = Arc(radius, 330 - start_angle)
        
        a.draw(canvas, at_point=canvas.center, rotation=angle)

