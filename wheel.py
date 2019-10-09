#!/usr/bin/env python
import random

from geometer import *


def draw(canvas):
    bound = int(canvas.width * 0.45)
    for deg_idx in range(72):
        for i in range(random.randint(35, 60)):
            deg = deg_idx * 5
            x = random.random() * bound
            r_bound = band(range(10, 80), x, bound, fuzz=True)
            r = random.random() * r_bound * 1.2
            canvas.set_fill_color(band(fills, x, bound, fuzz=True).midtone())
            Circle(r, Point(x, 0)).draw(canvas, at_point=canvas.center, rotation=deg)
