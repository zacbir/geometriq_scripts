#!/usr/bin/env python
from math import cos, pi, sin
import random

from geometer import *


def next_center_point_and_radius(center, radius):
    distance = random.random() * 0.3 + 0.6
    theta = random.random() * 2 * pi
    
    perimeter_x = distance * cos(theta) + center.x
    perimeter_y = distance * sin(theta) + center.y
    
    new_center_x = None
    new_center_y = None
    
    return Point(new_center_x, new_center_y)

def draw(canvas):
    radius = 1800
    center = canvas.center
    delta = 16
    
    while radius > 16:
        Circle(radius, center=center).draw(canvas)
        radius = radius - delta
        center = Point(center.x + delta, center.y)
