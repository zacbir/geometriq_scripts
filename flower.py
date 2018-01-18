from math import cos, radians, sin
import random

from geometer import *


def random_point_on_circle(center, radius):
    a = radians(random.random() * 360)
    x = center.x + radius * cos(a)
    y = center.y + radius * sin(a)
    return Point(x, y)


def draw(canvas):
    p1 = origin
    p2 = Point(canvas.width * 0.48, 0)

    cp_1 = random_point_on_circle(p1, 1000)
    cp_2 = random_point_on_circle(p2, 500)
    cp_3 = Point(cp_1.x, -1 * cp_1.y)
    cp_4 = Point(cp_2.x, -1 * cp_2.y)

    c = Curve([p1, p2], [cp_1], [cp_2])
    c2 = Curve([p1, p2], [cp_3], [cp_4])

    for p, color in enumerate(gradient(steps=45)):
        canvas.set_stroke_color(color.half())
        c.draw(canvas, at_point=canvas.center, rotation=p * 10)
        c2.draw(canvas, at_point=canvas.center, rotation=p * 10)
