from math import radians

from geometer import *

def draw(canvas):
    
    canvas.set_stroke_color(base1)
    canvas.set_fill_color(base03)
    canvas.fill_background()
    
    canvas.set_fill_color(clear)
    
    arc = Arc(1500, 180)
    arc.draw(canvas, at_point=canvas.center)
    arc.draw(canvas, at_point=canvas.center, rotation=radians(180))
    
    for i in range(31)[::-1]:
        arc = Arc(50 * i, 180, center=Point(1500 - 50 * i, 0))
        arc.draw(canvas, at_point=canvas.center
    
    for i in range(16)[::-1]:
        arc = Arc(100 * i, 180)
        arc.draw(canvas, at_point=canvas.center, rotation=180)
