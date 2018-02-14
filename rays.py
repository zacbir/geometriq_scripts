#!/usr/bin/env python
import random
from geometer import *


def draw(canvas):
    canvas.set_stroke_width(4)
    r = 512
    for d in range(360):
        color = band([violet] + fills, d, 360, fuzz=True)
        canvas.set_stroke_color(color.tint())        
        to = Point((random.random() * 0.4 + 0.6) * 2048 - 128, 0)
        center = Point((random.random() * 0.2 + 0.9) * r, 0)
        l = Line(to_point=to, center=center)
        l.draw(canvas, at_point=canvas.center, rotation=d)

