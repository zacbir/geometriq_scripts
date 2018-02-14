#!/usr/bin/env python

from geometer import *


def draw(canvas):
    # 
    for d in range(0, 360, 2):
        color = band([violet] + fills, d, 360)
        canvas.set_stroke_color(color.tint())
        a = Arc(d * 5, d)
        
        a.draw(canvas, at_point=canvas.center, rotation=d)
