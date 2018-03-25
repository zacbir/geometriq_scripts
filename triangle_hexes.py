from math import floor
import random
from geometer import *


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
    canvas.set_stroke_width(2)
    size = 512
    t = Triangle(size)
    g_east = VerticalHexagonGrid(canvas.center, size, 10, 10)
    g_west = VerticalHexagonGrid(Point(canvas.center.x + t.r, canvas.center.y + t.size / 2), size, 11, 12)

    g_snap = VerticalHexagonGrid(Point(canvas.center.x + t.r * 2, canvas.center.y), size, 12, 12)

    g_snap_large = VerticalHexagonGrid(g_snap.start, size * 2, 6, 6)

    for p in g_east.points:
        t = EastTriangle(size, p, g_snap)
        canvas.set_fill_color(color_for_point(p, canvas).midtone())
        t.draw(canvas)

    for p in g_west.points:
        t = WestTriangle(size, p, g_snap)
        canvas.set_fill_color(color_for_point(p, canvas).midtone())
        t.draw(canvas)

    for p in g_snap_large.points:
        step = 16
        for r in range(size)[::step]:
            h = VerticalHexagon(r, p)
            canvas.set_fill_color(clear)
            h.draw(canvas)
