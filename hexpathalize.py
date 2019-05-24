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
        
def draw(canvas):
    canvas.set_fill_color(black)
    canvas.fill_background()
    canvas.set_stroke_color(white)

    size = 32
    stroke_color = canvas.stroke_color

    reference_path = os.getenv("REFERENCE_IMAGE_PATH")

    reference = None
    if reference_path:
        reference = ReferenceImage(reference_path, canvas)

    g = VerticalHexagonGrid(canvas.center, size, floor(canvas.width / size), floor(canvas.height / size))
    # g = VerticalHexagonGrid(canvas.center, size, 6, 6)
    canvas.set_stroke_width(4)

    for p in g.points:

        # h = HorizontalHexagon(g.size - g.r, p)
        # h = HorizontalHexagon(size, p)
        h = HorizontalHexagon(g.step - g.r, p)

        reference_point = reference.transform_point(p)
        reference_color = reference.color_at_point(reference_point)
        reference_grey_idx = reference_color.greyscale().r  # point between 0.0-1.0, maps white-black

        canvas.set_stroke_color(stroke_color.alpha(reference_grey_idx))

        f = random.choice((three_left, three_right, two_up, two_pos, two_neg))
        operations = f(h)
        for shape, at, rotation in operations:
            if at:
                shape.draw(canvas, at_point=at, rotation=rotation)
            else:
                shape.draw(canvas)
