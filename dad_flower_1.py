#!/usr/bin/env python
from math import radians, sin, tan

from geometer import *

fills_cycle = fills[:] + fills[::-1]

def radius_ratio(angle):
    rad_angle = radians(angle)
    return (1 + tan(rad_angle)) / (1 - tan(rad_angle))


def initial_point(radius, angle):
    rad_angle = radians(angle)
    return Point(radius / sin(rad_angle), 0)


def draw(canvas):
    angle = 1.40625
    ratio = radius_ratio(angle)
    canvas.set_stroke_color(clear)
    play_center = canvas.random_point()
    
    for i in range(int(360 / (angle * 2))):
        radius = 2
        circle_center = initial_point(radius, angle)
        for j in range(100):
            c = Circle(radius, circle_center)
            #alpha = (j / 128.0)
            #print("j: {}, alpha: {}".format(j, alpha))
            canvas.set_fill_color(fills_cycle[j % 16].tint())
            #if j not in (1, 2):
            c.draw(canvas, at_point=play_center, rotation=i * angle * 2)
            circle_center = Point(circle_center.x + radius + radius * ratio, 0)
            radius = radius * ratio
        fills_cycle.append(fills_cycle.pop(0))
