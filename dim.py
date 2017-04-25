from math import sqrt

from geometer import *

def draw(canvas):
    
    background, stroke = base03, red
    
    canvas.set_stroke_color(green)
    canvas.set_fill_color(base03)
    
    canvas.fill_background()
    canvas.set_fill_color(clear)
    
    band_max = size = canvas.width**2
    
    a = 0
    while size > 10:
        canvas.set_stroke_color(band(fills, size, band_max))
        t = Triangle(size)
        t.draw(canvas, at_point=canvas.center(), rotation=radians(a * 2))
        a += 1
        size *= 0.90


