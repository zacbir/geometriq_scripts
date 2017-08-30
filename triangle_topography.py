from collections import deque
from math import atan, copysign, cos, pi, sin
import random

from geometer import *

t_fills = [base02, base1, base3, red]

initial_radius = 256
initial_area = 2 * pi * initial_radius


def shape_from(edge):
    """
    :param edge: Edge
    :return: ArbitraryTriangle

    Determine the cmp() difference between the opposite point and the intersection of a line
    through that point with an inverse slope with the edge's line. If the cmp is +1, we need
    to go in a negative direction from the intersection point. If negative, we need to go in
    a positive direction from the intersection point. The line we use to compute the intersection
    point is disposable.
    """
    line = edge.line
    A = line.center
    B = line.to_point
    C = edge.opposite_point

    intersection_line = Line.from_origin_with_slope(C, line.inverse_slope)
    intersection = line.intersection_with(intersection_line)

    position = -1 * cmp(C, intersection)

    new_point_intersection = line.point_from_center(random.random() * line.length)
    # new_point_intersection = line.midpoint
    new_point_line = Line.from_origin_with_slope(new_point_intersection, line.inverse_slope, position)

    new_area = random.random() * 0.25 * initial_area + initial_area

    new_height = min(new_area / (0.5 * line.length), initial_radius * 2)

    new_point = new_point_line.point_from_center(new_height)

    return ArbitraryTriangle([line.center, line.to_point, new_point])


def draw(canvas):

    canvas.set_stroke_color(clear)

    edges = deque()
    # points = []
    #
    # for j in range(3):
    #     angle_r = random.random() * pi * 2
    #     x = cos(angle_r) * initial_radius + canvas.center.x
    #     y = sin(angle_r) * initial_radius + canvas.center.y
    #     points.append(Point(x, y))

    a = NorthTriangle(initial_radius, canvas.center)
    edges.extend(a.edges)
    triangles_processed = 1

    canvas.set_fill_color(random.choice(t_fills).shade())
    a.draw(canvas)

    while len(edges) > 0:
        edge = edges.popleft()
        old_line = edge.line
        new_triangle = shape_from(edge)
        if not canvas.point_outside(new_triangle.center) and triangles_processed <= 9:
            edges.extend(new_triangle.edges[1:])
            triangles_processed += 1

        canvas.set_fill_color(random.choice(t_fills).shade())
        new_triangle.draw(canvas)
