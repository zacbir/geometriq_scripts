#!/usr/bin/env python

from geometer import *

def draw(canvas):
    
    step = canvas.width / 32
    
    canvas.set_stroke_width(8)
    
    cp = Point(0, canvas.height)
    
    for x in range(32):
        color = band(fills, x, 32, fuzz=True).midtone()
        canvas.set_stroke_color(color)
        c = Curve((Point(x * step, 0), Point(canvas.width, canvas.height - x * step)), [cp])
        c.draw(canvas)
    Curve((Point(canvas.width, 0), Point(canvas.width, 0)), [cp]).draw(canvas)
