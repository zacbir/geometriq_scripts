import random
from geometer import *


def line_at(x=None, y=None):
    if x is not None:
        return Line.from_origin_with_slope(Point(x, 0), None)
    elif y is not None:
        return Line.from_origin_with_slope(Point(0, y), 0)


def draw(canvas):
    c = Circle(1536, center=canvas.center)

    left_hand_points = set()
    left_hand_control_points = set()
    right_hand_points = set()
    right_hand_control_points = set()

    for y in range(0, canvas.height, 32):
        l = line_at(y=y)
        intersections = c.intersections_with_line(l)

        color = band(fills, y, canvas.height).midtone()

        if intersections is None or intersections[0] == intersections[1]:
            # not in the circle, or is tangent
            Line(center=Point(0, y), to_point=Point(canvas.width, y)).draw(canvas)
        else:
            left, right = intersections
            left_hand_points.add((left, color))
            left_hand_control_points.add(left)
            right_hand_points.add(right)
            right_hand_control_points.add(right)

            Line(center=Point(0, y), to_point=left).draw(canvas)
            Line(center=right, to_point=Point(canvas.width, y)).draw(canvas)

    for x in range(0, canvas.width, 32):
        lx = line_at(x=x)
        intersections = c.intersections_with_line(lx)

        if intersections is None or intersections[0] == intersections[1]:
            # not in the circle, or is tangent
            Line(center=Point(x, 0), to_point=Point(x, canvas.height)).draw(canvas)
        else:
            bottom, top = intersections

            Line(center=Point(x, 0), to_point=bottom).draw(canvas)
            Line(center=top, to_point=Point(x, canvas.height)).draw(canvas)

    for p in range(len(left_hand_points)):
        lhp, color = left_hand_points.pop()
        rhp = right_hand_points.pop()
        cp1 = left_hand_control_points.pop()
        cp2 = right_hand_control_points.pop()

        canvas.set_stroke_color(color)
        Curve([lhp, rhp], [cp1], [cp2]).draw(canvas)


