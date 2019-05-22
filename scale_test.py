#!/usr/bin/env python

from geometer import *


def draw(canvas):
    c = Circle(100)
    
    for x in (1, 2, 3, 4, 5):
        c.draw(canvas, scale_x=x)

