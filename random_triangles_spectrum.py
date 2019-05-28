from functools import cmp_to_key
import math
import random
from geometer import *


def nearest_points(points: set, point1: Point, point2: Point=None, count: int=1):
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
        midpoint = Line(point1, point2).midpoint

        def two_point_cmp(a: Point, b: Point):
            return a.distance_to(midpoint) - b.distance_to(midpoint)

        cmp_func = two_point_cmp
    else:
        def one_point_cmp(a: Point, b: Point):
            return a.distance_to(point1) - b.distance_to(point1)

        cmp_func = one_point_cmp

    sortable_points = list(other_points)

    nearest = sorted(sortable_points, key=cmp_to_key(cmp_func))

    return nearest[:count]


def position(point, line):
    """
    Determine the relative position (one side, or the other, or on) of a point to a line.

    :param point: Point
    :param line: Line
    :return: int
    """
    intersection_point = Line.from_origin_with_slope(point, line.inverse_slope).intersection_with(line)

    return -1 if point < intersection_point else 1 if point > intersection_point else 0


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

    chunk = 64

    points = set()
    edges = set()
    edge_lines_seen = {}
    all_lines_seen = set()

    iterations_x = int(math.floor(canvas.width / chunk))
    iterations_y = int(math.floor(canvas.height / chunk))

    points_per_chunk = 1

    for x_idx in range(iterations_x):

        for y_idx in range(iterations_y):

            chunk_min_x, chunk_max_x = x_idx * chunk, x_idx * chunk + chunk
            chunk_min_y, chunk_max_y = y_idx * chunk, y_idx * chunk + chunk

            xs = range(chunk_min_x, chunk_max_x)
            ys = range(chunk_min_y, chunk_max_y)

            chunk_points = [Point(x, y) for x, y in zip(random.sample(xs, points_per_chunk), random.sample(ys, points_per_chunk))]

            for p in chunk_points:
                points.add(p)

    prev_debug_value = canvas.debug
    canvas.debug = False

    # for p in points:
    #     canvas.set_fill_color(red)
    #     Circle(5, p).draw(canvas)

    # canvas.debug = prev_debug_value

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

        # prev_debug_value = canvas.debug
        # canvas.debug = False
        #
        # canvas.set_fill_color(yellow)
        # Circle(5, edge.line.midpoint).draw(canvas)
        #
        # canvas.debug = prev_debug_value

        opposite_position = edge.line.compare(edge.opposite_point)  # position(edge.opposite_point, edge.line)
        other_points = points - {p for p in points if edge.line.compare(p) == opposite_position}  # position(p, edge.line) == opposite_position}

        e_p1 = edge.line.center
        e_p2 = edge.line.to_point

        def intersects_with_any(test_lines, lines):
            for line in lines:
                for t_line in test_lines:
                    if t_line.intersects(line):
                        if t_line.intersection_with(line).is_basically(line.center) or t_line.intersection_with(line).is_basically(line.to_point):
                            return False
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
