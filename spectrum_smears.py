import random

from geometer import *

def draw(canvas):

    canvas.set_fill_color(base3)
    canvas.fill_background()

    strokes = [base03, base03, base03, base2, base2, base0]
    semi_strokes = [base1, base1, base1, base01, base01, base3]
    
    g = HorizontalHexagonGrid(canvas.center, 64, 75, 25)

    for p in g.points:

        line_length = random.random() * 256 + 128

        l = Line(Point(line_length / 2, 0), center=Point(- line_length / 2, 0))

        semi_stroke_color = band(semi_strokes, p.y, canvas.height)
        canvas.set_stroke_width(129)
        canvas.set_stroke_color(semi_stroke_color)

        l.draw(canvas, at_point=p, rotation=90)

        stroke_color = band(strokes, p.y, canvas.height)
        canvas.set_stroke_width(128)
        canvas.set_stroke_color(stroke_color.tint())

        l.draw(canvas, at_point=p, rotation=90)
