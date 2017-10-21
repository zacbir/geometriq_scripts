import math
import random
from geometer import *


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


def draw(canvas):
    """
    Make some pretty and draw it to `canvas`.

    :param canvas: CoreGraphicsCanvas
    :return: None
    """
    canvas.set_stroke_width(0.5)

    colors = [base1, base00, cyan, cyan, green, green]

    chunk = 128

    points = set()
    edges = set()
    edge_lines_seen = {}

    iterations_x = canvas.width / chunk
    iterations_y = canvas.height / chunk

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

    center_triangle_points = nearest_points(points, canvas.center, count=3)

    a = ArbitraryTriangle(center_triangle_points)
    canvas.set_fill_color(random.choice(colors).midtone())

    a.draw(canvas)

    edges.update(set(a.edges))
    edge_lines_seen.update({x.line: 1 for x in a.edges})

    while edges:
        edge = edges.pop()

        if edge_lines_seen.setdefault(edge.line, 0) >= 2:
            continue

        edge_lines_seen[edge.line] += 1

        opposite_position = position(edge.opposite_point, edge.line)

        invalid_points = filter(lambda x: position(x, edge.line) == opposite_position, list(points))

        other_points = points - set(invalid_points)
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
            # while intersects_with_any({Line(e_p1, n_p3), Line(e_p2, n_p3)}, edge_lines_seen.keys()):
            #     other_points = other_points - {n_p3}
            #     n_p3 = nearest_points(other_points, e_p1, e_p2)[0]

            at = ArbitraryTriangle([e_p1, e_p2, n_p3])
            canvas.set_fill_color(random.choice(colors).midtone())

            at.draw(canvas)

            new_edge_1 = Edge(Line(e_p1, n_p3), e_p2)
            new_edge_2 = Edge(Line(e_p2, n_p3), e_p1)
            edge_lines_seen[new_edge_1.line] = edge_lines_seen.setdefault(new_edge_1.line, 0) + 1
            edge_lines_seen[new_edge_2.line] = edge_lines_seen.setdefault(new_edge_2.line, 0) + 1
            edges.update({new_edge_1, new_edge_2})

        except IndexError:
            continue
