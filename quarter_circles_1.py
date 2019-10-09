#!/usr/bin/env python

from math import floor
from random import *
from geometer import *

def pos_slope(point, size):
    return(
        (Point(point.x - size / 2.0,
               point.y - size / 2.0),
         0),
        (Point(point.x + size / 2.0,
               point.y + size / 2.0),
         180))

def neg_slope(point, size):
    return(
        (Point(point.x + size / 2.0,
               point.y - size / 2.0),
         90),
        (Point(point.x - size / 2.0,
               point.y + size / 2.0),
         270))
        
size = 64

a = QuarterCircle(size / 2.0)
s = Square(size)
c = Circle(8)

def draw(canvas):
    g = SquareGrid(canvas.center, size, floor(canvas.width / size), floor(canvas.height / size))
    color_center = canvas.random_point()
    longest = canvas.longest_distance_from(color_center)
    canvas.set_stroke_width(16)

    for p in g.points:
        d = p.distance_to(color_center)

        canvas.set_stroke_color(band(fills, d, longest, fuzz=True))
        # canvas.set_stroke_color(green)
        # c.draw(canvas, at_point=p)
        # canvas.set_stroke_color(red)
        # s.draw(canvas, at_point=p)
        # canvas.set_stroke_color(base3)
        f = random.choice((pos_slope, neg_slope))
        points_and_rotations = f(p, size)
        for p1, r in points_and_rotations:
            a.draw(canvas, at_point=p1, rotation=r)

