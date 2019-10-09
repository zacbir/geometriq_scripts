#!/usr/bin/env python
import random

from geometer import *


def draw(canvas):
    
    xs = random.sample(range(100, canvas.width - 100), 50)
    ys = random.sample(range(100, canvas.height - 100), 50)
    
    for x in xs:
        start = Point(x, 100)
        end = Point(x, canvas.height - 100)
        stroke = band(fills, x - 100, canvas.width - 200, fuzz=True)
        canvas.set_stroke_color(stroke.midtone())
        Line(start, end).draw(canvas)
        
    for y in ys:
        start = Point(100, y)
        end = Point(canvas.width - 100, y)
        stroke = band(fills, y - 100, canvas.height - 200, fuzz=True)
        canvas.set_stroke_color(stroke.midtone())
        Line(start, end).draw(canvas)

