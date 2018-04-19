#!/usr/bin/env python
import random
from geometer import *


def draw(canvas):
    canvas.set_line_cap(kCGLineCapButt)

    base_radius = 1024
    segments = 24

    degree_starts = sorted(random.sample(range(358), segments))
    start = 0

    for d in degree_starts:
        thickness = random.randrange(2, 512, 2)
        canvas.set_stroke_width(thickness)
        arc_angle = d - start
        a = Arc(base_radius - (thickness / 2), arc_angle)
        
        a.draw(canvas, at_point=canvas.center, rotation=start)

        start = d + 2  # leave a two-degree gap

    arc_angle = 358 - start  # leave a two-degree gap to 0
    thickness = random.randrange(2, 512, 2)
    canvas.set_stroke_width(thickness)
    a = Arc(base_radius - (thickness / 2), arc_angle)

    a.draw(canvas, at_point=canvas.center, rotation=start)
