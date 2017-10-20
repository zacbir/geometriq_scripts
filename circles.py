import random
from geometer import *


def draw_circles(canvas, count, radius, point):

    canvas.set_stroke_color(random.choice(fills).midtone())
    canvas.set_stroke_width(random.random() * 128 + 16)

    for i in range(count):

        Circle(radius * i + radius, point).draw(canvas)


def draw(canvas):

    for c in range(32):

        p = canvas.random_point()

        rnd = random.random()

        radius = random.random() * canvas.width * 0.125

        if rnd < 0.25:
            draw_circles(canvas, 2, radius, p)
        elif 0.25 <= rnd < 0.75:
            draw_circles(canvas, 1, radius, p)
        else:
            draw_circles(canvas, 3, radius, p)
