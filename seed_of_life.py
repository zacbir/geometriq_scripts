from math import radians

from geometer import *

def draw(canvas):
    canvas.set_fill_color(base03)
    canvas.set_stroke_color(base1)

    canvas.fill_background()

    canvas.set_fill_color(clear)

    t = Triangle(512)
    t.draw(canvas, at_point=canvas.center(), rotation=radians(180))
    t2 = Triangle(256)
    t2.draw(canvas, at_point=canvas.center())

    circle = Circle(t.r)
    grid = VerticalHexagonGrid(canvas.center(), t.r, 2, 2)

    for point in grid.points:
        circle.draw(canvas, at_point=point)

    circle.draw(canvas, at_point=canvas.center())

