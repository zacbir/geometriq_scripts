import random

from geometer import *


def random_point_within(min_x, max_x, min_y, max_y):
    rand_x = random.random() * (max_x - min_x) + min_x
    rand_y = random.random() * (max_y - min_y) + min_y

    return Point(rand_x, rand_y)


def draw(canvas):

    blocks = 3

    bounds_w = canvas.width / (blocks * 2.0 + 1)
    bounds_h = canvas.height / (blocks * 2.0 + 1)

    for plot_w_idx in range(blocks):
        for plot_h_idx in range(blocks):
            min_x = plot_w_idx * bounds_w * 2 + bounds_w
            max_x = plot_w_idx * bounds_w * 2 + bounds_w * 2

            min_y = plot_h_idx * bounds_h * 2 + bounds_h
            max_y = plot_h_idx * bounds_h * 2 + bounds_h * 2

            points = []
            control_points = []

            for x in range(3): #random.choice([3, 4, 5])):
                points.append(random_point_within(min_x, max_x, min_y, max_y))
                control_points.append(random_point_within(min_x, max_x, min_y, max_y))

            c = Curve(points, control_points)
            c.draw(canvas)
