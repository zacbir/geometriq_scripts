#!/usr/bin/env python
import random

from geometer import *


def draw(canvas):
    radius = 1800
    center = canvas.center
    delta = 16
    
    while radius > 16:
        Circle(radius, center=center).draw(canvas)
        radius = radius - delta
        center = Point(center.x + delta, center.y)

