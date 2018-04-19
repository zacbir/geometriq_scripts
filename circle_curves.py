import random
from geometer import *

def line_at(y):
    return Line.from_origin_with_slope(Point(0, y), 0)

def draw(canvas):
    c = Circle(1536, center=canvas.center)

    left_hand_points = set()
    left_hand_control_points = set()
    right_hand_points = set()
    right_hand_control_points = set()

    for y in range(0, canvas.height, 16):
        l = line_at(y)
        intersections = c.intersections_with_line(l)

        color = band(fills, y, canvas.height).midtone()

        if intersections is not None and intersections[0] != intersections[1]:
            left, right = intersections
            left_hand_points.add((left, color))
            left_hand_control_points.add(left)
            right_hand_points.add(right)
            right_hand_control_points.add(right)

    for p in range(len(left_hand_points)):
        lhp, color = left_hand_points.pop()
        rhp = right_hand_points.pop()
        cp1 = left_hand_control_points.pop()
        cp2 = right_hand_control_points.pop()

        canvas.set_stroke_color(color)
        Curve([lhp, rhp], [cp1], [cp2]).draw(canvas)

