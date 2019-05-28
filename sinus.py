#!/usr/bin/env python
from math import pi, sin
import random

from geometer import *


tau = 2 * pi


def draw(canvas):
    
    p = Point(canvas.width / 128, canvas.height / 128)
    
    factor = 64  # random.random() * 128
    
    for x in range(31):
        Line(center=Point(x * 2, sin(x)), to_point=Point(x * 2, -1 * sin(x))).draw(canvas, at_point=p, scale_x=factor)
