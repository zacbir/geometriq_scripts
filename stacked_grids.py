from math import floor
import random

from geometer import *


def draw(canvas):
    canvas.set_stroke_width(random.random() * 0.4 + 0.1)
    x_offset = canvas.width / 20
    y_offset = canvas.height / 20
    p1 = Point(x_offset, canvas.center.y)
    p2 = Point(canvas.width - x_offset, canvas.center.y)

    x = random.random() * canvas.width / 3.0 + canvas.width / 6.0

    sheets = 8

    for i in range(sheets):
        canvas.set_stroke_color(base1.hair())  # alpha(random.random() * 0.5 + 0.25))
        x += 100
        y = (canvas.height / sheets) * i + y_offset
        p3 = Point(x, y)

        line1 = Line(center=p3, to_point=p1)
        line1.extended().draw(canvas)
        left_lines = [line1]

        line2 = Line(center=p3, to_point=p2)
        line2.extended().draw(canvas)
        right_lines = [line2]

        left_distances = sorted(random.sample(range(int(floor(line1.length))), 5))
        left_points = [line1.point_from_center(d) for d in left_distances]
        right_lines.extend([Line(center=l_p, to_point=p2) for l_p in left_points])

        right_distances = sorted(random.sample(range(int(floor(line2.length))), 5))
        right_points = [line2.point_from_center(d) for d in right_distances]
        left_lines.extend([Line(center=r_p, to_point=p1) for r_p in right_points])

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
                canvas.set_fill_color(fill.half())  # alpha(1.0 / sheets))

                s.draw(canvas)
