import random
from geometer import *

def line_at(y):
    return Line.from_origin_with_slope(Point(0, y), 0)

def draw(canvas):
    c = Circle(1536, center=canvas.center)

    left_hand_points = set()
    right_hand_points = set()

    for y in range(0, canvas.height, 32):
        l = line_at(y)
        intersections = c.intersections_with_line(l)

        color = band(fills, y, canvas.height) # .midtone()

        canvas.set_stroke_color(color)

        if intersections is None:
            # draw the line
            Line(center=Point(0, y), to_point=Point(canvas.width, y)).draw(canvas)
        elif intersections[0] == intersections[1]:
            # tangent
            Line(center=Point(0, y), to_point=Point(canvas.width, y)).draw(canvas)
        else:
            left, right = intersections
            left_hand_points.add((left, color))
            right_hand_points.add(right)

            Line(center=Point(0, y), to_point=left).draw(canvas)

    for p in range(len(left_hand_points)):
        lhp, color = left_hand_points.pop()
        rhp = right_hand_points.pop()

        canvas.set_stroke_color(color)
        Line(center=lhp, to_point=rhp).draw(canvas)
        Line(center=rhp, to_point=Point(canvas.width, rhp.y)).draw(canvas)

