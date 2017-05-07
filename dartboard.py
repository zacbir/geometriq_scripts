from math import sqrt

from geometer import *

def draw(canvas):

    strokes = [red.alpha(0.75), red.half(), red.alpha(0.25)]

    radius_step = 50
    canvas.set_stroke_width(50)
    canvas.set_line_cap(kCGLineCapButt)

    max_diagonal = sqrt((canvas.width / 2)**2 + (canvas.height / 2)**2)

    for i in range(60):

        start_idx = i % 3
        radius = i * radius_step

        a = Arc(radius, 5)

        for j in range(72):
            stroke = strokes[j % 3 - start_idx]
            canvas.set_stroke_color(stroke)
            a.draw(canvas, at_point=canvas.center, rotation=5 * j)
