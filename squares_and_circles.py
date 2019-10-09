#!/usr/bin/env python
import random

from geometer import *


def offset(point, x, y):
    return Point(point.x + x, point.y + y)


def draw(canvas):
    canvas.set_stroke_width(0)
    canvas.set_stroke_color(clear)
    
    grid_1 = SquareGrid(canvas.center, 64, 32, 32)
    
    grid_2 = SquareGrid(offset(canvas.center, 32, 32), 128, 17, 17)
    
    for p in grid_1.points:
        canvas.set_fill_color(random.choice((base3, base03)))
        Square(64).draw(canvas, at_point=p)
        
    for p in grid_2.points:
        
        #canvas.set_stroke_color(red)
        #canvas.set_stroke_width(1)
        #canvas.set_fill_color(clear)
        canvas.set_fill_color(random.choice((base3, base03)))
        Circle(64).draw(canvas, at_point=p)

