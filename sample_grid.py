import random
import string

from geometer import *


def gen_points():

    local_points = {}

    point_names = [c for c in string.ascii_lowercase[:9]]

    chunk = 5
    points_per_chunk = 1

    scale = 100

    for x_idx in range(3):

        for y_idx in range(3):

            chunk_min_x, chunk_max_x = x_idx * chunk + 1, x_idx * chunk + chunk
            chunk_min_y, chunk_max_y = y_idx * chunk + 1, y_idx * chunk + chunk

            xs = range(chunk_min_x, chunk_max_x)
            ys = range(chunk_min_y, chunk_max_y)

            chunk_points = [Point(x * scale, y * scale) for x, y in
                            zip(random.sample(xs, points_per_chunk), random.sample(ys, points_per_chunk))]

            for p in chunk_points:
                name = point_names.pop(0)
                local_points[name] = p

    return local_points


points = gen_points()
