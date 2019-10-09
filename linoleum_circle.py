import random

from geometer import *


def draw(canvas):

    canvas.set_stroke_color(clear)
    background_radius = canvas.diagonal * 0.6

    for x in range(int(360 / 5)):

        segment = CircleSegment(background_radius, 5)

        rotation = x * 5

        fill = band(fills[::-1], rotation, 360, fuzz=True)
        canvas.set_fill_color(fill.midtone())

        segment.draw(canvas, at_point=canvas.center, rotation=rotation)

    foreground_radius = canvas.diagonal * 0.3

    circle = Circle(foreground_radius)
    canvas.set_fill_color(base03)
    circle.draw(canvas, at_point=canvas.center)

    for y in range(int(360 / 10)):

        segment = CircleSegment(foreground_radius, 10)

        rotation = 10 * y

        fill = band(fills, rotation, 360, fuzz=True)
        canvas.set_fill_color(fill.midtone())

        segment.draw(canvas, at_point=canvas.center, rotation=rotation)
