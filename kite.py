from math import floor
import random

from geometer import *


def draw(canvas):
    canvas.set_stroke_width(random.random() * 0.4 + 0.1)
    x_offset = canvas.width / 20
    y_offset = canvas.height / 20
    p1 = Point(x_offset, canvas.center.y)
    p2 = Point(canvas.width - x_offset, canvas.center.y)

    x = random.random() * canvas.width / 2.0 + canvas.width / 4.0
    
    sheets = 50
    move_direction = 1 if x < canvas.width / 2 else -1
    move = (canvas.width - x) / sheets * move_direction

    for i in range(sheets):
        canvas.set_stroke_color(base1.hair())  # alpha(random.random() * 0.5 + 0.25))
        y = (canvas.height / sheets) * i + y_offset
        x += move
        p3 = Point(x, y)

        line1 = Line(center=p3, to_point=p1)
        line1.extended().draw(canvas)
        left_lines = [line1]

        line2 = Line(center=p3, to_point=p2)
        line2.extended().draw(canvas)
        right_lines = [line2]

        short_side = min(line1.length, line2.length)
        chunk = short_side / (sheets * 1.1)
        square_side = chunk * i + chunk
        right_lines.append(Line(center=line1.point_from_center(square_side), to_point=p2))
        left_lines.append(Line(center=line2.point_from_center(square_side), to_point=p1))

        left_pairs = [left_lines[l:l + 2] for l in range(0, len(left_lines), 2)]
        right_pairs = [right_lines[r:r + 2] for r in range(0, len(right_lines), 2)]

        for r1, r2 in right_pairs:

            r1.extended().draw(canvas)
            r2.extended().draw(canvas)

            for l1, l2 in left_pairs:

                s = Shape(0)

                s.points = [
                    l1.intersection_with(r1),
                    l1.intersection_with(r2),
                    l2.intersection_with(r2),
                    l2.intersection_with(r1)
                ]

                l1.extended().draw(canvas)
                l2.extended().draw(canvas)

                fill = band(fills, i, sheets)
                canvas.set_fill_color(fill.half())

                s.draw(canvas)
