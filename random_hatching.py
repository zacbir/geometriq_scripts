import random
from math import ceil

from geometer import *


def draw(canvas):
    size = 64

    g = SquareGrid(canvas.center, size, ceil(canvas.width / size), ceil(canvas.height / size))

    reference_line = Line.from_origin_with_slope(origin, -(2.0 / 5.0))
    reference_point = canvas.random_point()
    longest_line = canvas.longest_distance_from(reference_point)

    canvas.set_stroke_width(8)

    for p in g.points:

        d = reference_point.distance_to(p)

        fill = band(fills, d, longest_line, fuzz=True)

        canvas.set_stroke_color(fill.midtone())

        angle = random.random() * 180

        segment0 = Line(Point(-(size / 2), 0), Point((size / 2), 0))

        segment0.draw(canvas, at_point=p, rotation=angle)

        segment1 = Line(Point(-(size / 2), -(size / 4)), Point((size / 2), -(size / 4)))

        segment1.draw(canvas, at_point=p, rotation=angle)

        segment2 = Line(Point(-(size / 2), (size / 4)), Point((size / 2), (size / 4)))

        segment2.draw(canvas, at_point=p, rotation=angle)

