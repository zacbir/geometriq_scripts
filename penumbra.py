#!/usr/bin/env python
import random

from geometer import *


def draw(canvas):
    
    radius = 1024
    
    for r in range(360 * 12):
        
        d = float(r / 12)
        above = random.random() * 1024
        below = -1 * random.random() * 1024
        
        line_color = band(fills, d, 360, fuzz=True)
        canvas.set_stroke_color(line_color.shade())
        canvas.set_stroke_width(random.random())
        
        # chance = random.random()
        # if chance < 0.15:
        #     x = radius - random.random() * 250
        # elif chance > 0.85:
        #     x = radius + random.random() * 500
        # else:
        #     x = radius

        Line(center=Point(radius, above), to_point=Point(radius, below)).draw(canvas, at_point=canvas.center, rotation=d)

