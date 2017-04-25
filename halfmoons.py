import random

from geometer import *

background, stroke = base03, yellow

def draw(canvas):
    canvas.set_stroke_color(clear)
    canvas.set_fill_color(background)
    canvas.fill_background()

    center = canvas.center

    size = 128

    h = HalfCircle(size)

    grid1 = SquareGrid(Point(center.x, center.y + size / 2), size * 2, 6, 6)
    grid2 = SquareGrid(Point(center.x, center.y - size / 2), size * 2, 6, 6)

    for point in grid1.points.union(grid2.points):
        canvas.set_fill_color(stroke.alpha(random.random() * 1.0))
        h.draw(canvas, at_point=point, rotation=90)
        canvas.set_fill_color(stroke.alpha(random.random() * 1.0))
        h.draw(canvas, at_point=point, rotation=-90)

