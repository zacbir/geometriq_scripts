from math import floor
import random
from geometer import *


def color_for_point(point, canvas):
    """

    :param point: Point
    :param canvas: CoreGraphicsCanvas
    :return: Color
    """
    line = Line.from_origin_with_slope(origin, 0)
    distance = line.distance_to(point)
    opacity = random.choice([0.25, 0.5, 0.75])
    return band([violet] + fills, distance, canvas.height, fuzz=True).alpha(opacity)


def thickness_for_point(point, canvas):
    """

    :param point:
    :param canvas:
    :return:
    """
    return band(list(range(4, 256, 32)), point.x, canvas.width, fuzz=True)


def draw(canvas):
    canvas.set_stroke_width(4)
    canvas.set_stroke_color(base03)
    size = 128
    t = Triangle(size)
    g_east = VerticalHexagonGrid(canvas.center, size, 26, 12)
    g_west = VerticalHexagonGrid(Point(canvas.center.x + t.r, canvas.center.y + t.size / 2), size, 28, 14)

    g_snap = VerticalHexagonGrid(Point(canvas.center.x + t.r * 2, canvas.center.y), size, 28, 14)

    g_snap_large = HorizontalHexagonGrid(g_snap.start, t.step * 2, 28, 16)

    for p in g_east.points:
        t = EastTriangle(size, p, g_snap)
        canvas.set_fill_color(color_for_point(p, canvas))
        t.draw(canvas)

    for p in g_west.points:
        t = WestTriangle(size, p, g_snap)
        canvas.set_fill_color(color_for_point(p, canvas))
        t.draw(canvas)

    for p in g_snap_large.points:
        canvas.set_fill_color(clear)
        h = VerticalHexagon(size, p)
        canvas.set_stroke_width(thickness_for_point(p, canvas))
        h.draw(canvas)
