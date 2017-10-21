import math
import random
from geometer import *

from . import sample_grid


def nearest_points(points, point1, point2=None, count=1):
    """
    Find the nearest point(s) to either a single point `point1`, or to the midpoint of a line between `point1` and `point2`.

    :param points: set[Point]
    :param point1: Point
    :param point2: Point
    :param count: int
    :return: list[Point]
    """
    other_points = points - {point1}

    if point2:
        other_points.discard(point2)
        l = Line(point1, point2)
        nearest = sorted(list(other_points), lambda a, b: cmp(a.distance_to(l.midpoint), b.distance_to(l.midpoint)))
    else:
        nearest = sorted(list(other_points), lambda a, b: cmp(a.distance_to(point1), b.distance_to(point1)))

    return nearest[:count]


def position(point, line):
    """
    Determine the relative position (one side, or the other, or on) of a point to a line.

    :param point: Point
    :param line: Line
    :return: int
    """
    intersection_point = Line.from_origin_with_slope(point, line.inverse_slope).intersection_with(line)

    return cmp(point, intersection_point)


def color_for_point(point, canvas):
    """

    :param point: Point
    :param canvas: CoreGraphicsCanvas
    :return: Color
    """
    line = Line.from_origin_with_slope(Point(canvas.width, 0), 2.0/5.0)
    distance = line.distance_to(point)
    return band(fills, distance, canvas.diagonal, fuzz=True)


def draw(canvas):
    """
    Make some pretty and draw it to `canvas`.

    :param canvas: CoreGraphicsCanvas
    :return: None
    """
    canvas.set_stroke_width(0.5)

    chunk = 32

    points = set()
    edges = set()
    edge_lines_seen = {}
    all_lines_seen = set()

    iterations_x = canvas.width / chunk
    iterations_y = canvas.height / chunk

    points_per_chunk = 1

    sample_points = {
        'a': Point(x=100, y=100),
        'b': Point(x=400, y=700),
        'c': Point(x=300, y=1300),
        'd': Point(x=900, y=300),
        'e': Point(x=700, y=900),
        'f': Point(x=800, y=1100),
        'g': Point(x=1300, y=200),
        'h': Point(x=1300, y=600),
        'i': Point(x=1300, y=1400)
    }

    points = set(sample_points.values())
    # points = {
    #     sample_points['l'],
    #     sample_points['m'],
    #     sample_points['n'],
    #     sample_points['q'],
    #     sample_points['r'],
    #     sample_points['s'],
    # }

    prev_debug_value = canvas.debug
    canvas.debug = False

    for p in sample_points.values():
        canvas.set_fill_color(red)
        Circle(5, p).draw(canvas)

    canvas.debug = prev_debug_value

    center_triangle_points = nearest_points(points, canvas.center, count=3)

    a = ArbitraryTriangle(center_triangle_points)
    fill = color_for_point(a.center, canvas)
    canvas.set_fill_color(fill.midtone())

    a.draw(canvas)

    edges.update(set(a.edges))
    edge_lines_seen.update({x.line: 1 for x in a.edges})
    all_lines_seen.update({x.line for x in a.edges})

    while edges:
        edge = edges.pop()

        if edge_lines_seen.setdefault(edge.line, 0) >= 2:
            continue

        edge_lines_seen[edge.line] += 1

        prev_debug_value = canvas.debug
        canvas.debug = False

        canvas.set_fill_color(yellow)
        Circle(5, edge.line.midpoint).draw(canvas)

        canvas.debug = prev_debug_value

        opposite_position = position(edge.opposite_point, edge.line)
        other_points = points - {p for p in points if position(p, edge.line) == opposite_position}

        e_p1 = edge.line.center
        e_p2 = edge.line.to_point

        def intersects_with_any(test_lines, lines):
            for line in lines:
                for t_line in test_lines:
                    if t_line.intersects(line):
                        return True

            return False

        try:
            n_p3 = nearest_points(other_points, e_p1, e_p2)[0]
            # candidate_points = nearest_points(other_points, e_p1, e_p2, count=None)
            # n_p3 = candidate_points.pop(0)
            # while intersects_with_any({Line(e_p1, n_p3), Line(e_p2, n_p3)}, all_lines_seen):
            #     n_p3 = candidate_points.pop(0)

            at = ArbitraryTriangle([e_p1, e_p2, n_p3])

            # d = angle_from(at.center, to=canvas.center)
            # fill_idx = d
            fill = color_for_point(at.center, canvas)
            # fill = band(fills, at.center.x, canvas.width, fuzz=True)     
            canvas.set_fill_color(fill.midtone())

            at.draw(canvas)

            new_edge_1 = Edge(Line(e_p1, n_p3), e_p2)
            new_edge_2 = Edge(Line(e_p2, n_p3), e_p1)
            edge_lines_seen[new_edge_1.line] = edge_lines_seen.setdefault(new_edge_1.line, 0) + 1
            edge_lines_seen[new_edge_2.line] = edge_lines_seen.setdefault(new_edge_2.line, 0) + 1
            edges.update({new_edge_1, new_edge_2})
            all_lines_seen.update({new_edge_1.line, new_edge_2.line})

        except IndexError:
            continue
