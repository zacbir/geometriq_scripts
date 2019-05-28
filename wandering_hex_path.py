#!/usr/bin/env python

from math import floor
from random import *

from geometer import *


def three_right(hex):
    points = hex.points
    return (
        (Arc(hex.size / 2, 120), points[1], 120),
        (Arc(hex.size / 2, 120), points[3], 0),
        (Arc(hex.size / 2, 120), points[5], -120)
    )

def three_left(hex):
    points = hex.points
    return (
        (Arc(hex.size / 2, 120), points[0], 180),
        (Arc(hex.size / 2, 120), points[2], 60),
        (Arc(hex.size / 2, 120), points[4], -60)
    )

def two_up(hex):
    points = hex.points
    return (
        (Arc(hex.size / 2, 120), points[4], -60),
        (Line(
            Line(points[2], points[3]).midpoint,
            Line(points[0], points[5]).midpoint), None, None),
        (Arc(hex.size / 2, 120), points[1], 120)
    )

def two_pos(hex):
    points = hex.points
    return (
        (Arc(hex.size / 2, 120), points[5], -120),
        (Line(
            Line(points[0], points[1]).midpoint,
            Line(points[3], points[4]).midpoint), None, None),
        (Arc(hex.size / 2, 120), points[2], 60)
    )

def two_neg(hex):
    points = hex.points
    return (
        (Arc(hex.size / 2, 120), points[0], 180),
        (Line(
            Line(points[1], points[2]).midpoint,
            Line(points[4], points[5]).midpoint), None, None),
        (Arc(hex.size / 2, 120), points[3], 0)
    )
        
size = 64

def draw(canvas):
    g = VerticalHexagonGrid(canvas.center, size, floor(canvas.width / size), floor(canvas.height / size))
    # g = VerticalHexagonGrid(canvas.center, size, 6, 6)
    color_center = canvas.random_point()
    longest = canvas.longest_distance_from(color_center)
    canvas.set_stroke_width(16)

    for p in g.points:
        d = p.distance_to(color_center)

        # h = HorizontalHexagon(g.size - g.r, p)
        # h = HorizontalHexagon(size, p)
        h = HorizontalHexagon(g.step - g.r, p)

        canvas.set_stroke_color(band(fills, d, longest, fuzz=True))

        f = random.choice((three_left, three_right, two_up, two_pos, two_neg))
        operations = f(h)
        for shape, at, rotation in operations:
            if at:
                shape.draw(canvas, at_point=at, rotation=rotation)
            else:
                shape.draw(canvas)
