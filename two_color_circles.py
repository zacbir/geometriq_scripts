import random

from geometer import *

def draw(canvas):
    canvas.set_fill_color(clear)

    iterations = 30

    for d in range(iterations):
        stroke = band(fills, d, iterations)
        radius = d * 100
        canvas.set_stroke_width(50)
        canvas.set_stroke_color(stroke.half())
        c = Circle(radius)
        c.draw(canvas, at_point=canvas.center)
        canvas.set_stroke_color(stroke.shade())
        a = Arc(radius, angle=180)
        a.draw(canvas, at_point=canvas.center, rotation=random.random() * 30 - 15)
