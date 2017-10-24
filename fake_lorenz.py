from functools import partial
import random

from geometer import *


def random_point_within(min_x, max_x, min_y, max_y):
    rand_x = random.random() * (max_x - min_x) + min_x
    rand_y = random.random() * (max_y - min_y) + min_y

    return Point(rand_x, rand_y)


def draw(canvas):
    upper_left = partial(random_point_within, 0, canvas.width / 2.0, canvas.height / 2.0, canvas.height)
    upper_right = partial(random_point_within, canvas.width / 2.0, canvas.width, canvas.height / 2.0, canvas.height)
    lower_left = partial(random_point_within, 0, canvas.width / 2.0, 0, canvas.height / 2.0)
    lower_right = partial(random_point_within, canvas.width / 2.0, canvas.width, 0, canvas.height / 2.0)

    t = NorthTriangle(canvas.width * 0.66, canvas.center)

    for i in range(16):
        p_1 = lower_left()
        p_2 = upper_right()
        p_3 = lower_right()
        c = Curve(t.points + [t.points[0]], [p_1, p_2, p_3, p_1])
        c.draw(canvas)
