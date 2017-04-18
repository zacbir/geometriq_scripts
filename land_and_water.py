from math import radians

from geometer import *

def draw(canvas):
    
    canvas.set_stroke_color(base1)
    canvas.set_fill_color(base03)
    canvas.fill_background()
    
    canvas.set_fill_color(clear)
    
    hc = HalfCircle(1500)
    canvas.set_fill_color(orange)
    hc.draw(canvas, at_point=canvas.center)
    canvas.set_fill_color(blue)
    hc.draw(canvas, at_point=canvas.center, rotation=radians(180))
    
    for i in range(11)[::-1]:
        hc = HalfCircle(150 * i, center=Point(1500 - 150 * i, 0))
        canvas.set_fill_color(yellow.alpha(0.5 - i / 20))
        hc.draw(canvas, at_point=canvas.center, rotation=radians(0))
        canvas.set_fill_color(cyan.alpha(0.5 - i / 20))
        hc.draw(canvas, at_point=canvas.center, rotation=radians(180))

