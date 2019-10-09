#!/usr/bin/env python

from geometer import *


stroke = 64
length = 80


def stroke_and_length(canvas, point):
    percentage = (canvas.height - point.y) / canvas.height
    return stroke * percentage, length * percentage
    

def draw(canvas):
    g = DiamondGrid(canvas.center, 128, 5, 5)
    
    for p in g.points:
        Circle(32, p).draw(canvas)
        continue
        s, l = stroke_and_length(canvas, p)
        canvas.set_stroke_width(s)
        Line(Point(p.x - l / 2, p.y), Point(p.x + l / 2, p.y)).draw(canvas)

