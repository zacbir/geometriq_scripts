from math import atan, copysign, cos, pi, sin
import random

from geometer import *

t_fills = [base02, base1, base3, red]

edges_seen = set()


def shape_from(edge):
    """
    :param edge: Edge
    :return: ArbitraryTriangle
    """
    line = edge.line
    A = line.center
    B = line.to_point
    C = edge.opposite_point
    position = ((B.x - A.x) * (C.y - A.y) - (B.y - A.y) * (C.x - A.x))

    rad_slope = atan(line.slope)

    angle_r = copysign(rad_slope + random.random() * pi, position)

    radius = line.length / 2
    x = cos(angle_r) * radius + line.midpoint.x
    y = sin(angle_r) * radius + line.midpoint.y

    return ArbitraryTriangle([line.center, line.to_point, Point(x, y)])


def draw_further(canvas, triangle):
    if len(edges_seen) > 9:
        return

    for edge in triangle.edges:
        if edge.line not in edges_seen:
            edges_seen.add(edge.line)
            new_triangle = shape_from(edge)

            canvas.set_fill_color(random.choice(t_fills).shade())
            new_triangle.draw(canvas)

            draw_further(canvas, new_triangle)


def draw(canvas):

    canvas.set_stroke_color(clear)

    points = []

    radius = 1024

    for j in range(3):
        angle_r = random.random() * pi * 2
        x = cos(angle_r) * radius + canvas.center.x
        y = sin(angle_r) * radius + canvas.center.y
        points.append(Point(x, y))

    a = ArbitraryTriangle(points)

    canvas.set_fill_color(random.choice(t_fills).shade())
    a.draw(canvas)

    draw_further(canvas, a)
