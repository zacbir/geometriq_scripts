#!/usr/bin/env python

from geometer import *

def intersect_for(x, line):
    vert = Line.from_origin_with_slope(Point(x, 0), None)
    return vert.intersection_with(line)

def draw(canvas):
    cp = Point(0, canvas.height)
    diag = Line.from_origin_with_slope(cp, -1)
    starts = [Point(x, 0) for x in range(0, canvas.width, 100)]
    ends = [intersect_for(x, diag) for x in list(range(100, canvas.width, 100)) + [canvas.width]]
    for idx, s in enumerate(starts):
        color = band(fills, s.x, canvas.width, fuzz=True).midtone()
        canvas.set_stroke_color(color)
        c = Curve((s, ends[idx]), [cp])
        c.draw(canvas)
