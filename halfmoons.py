from math import radians
import random

from geometer import *

width = 4096
height = 4096

background, stroke = base03, yellow

canvas = CoreGraphicsCanvas('output/halfmoons', width, height)
canvas.set_stroke_color(clear)
canvas.set_fill_color(background)
canvas.fill_background()

center = canvas.center()

size = 128

h = HalfCircle(size)

grid1 = SquareGrid(Point(center.x, center.y + size / 2), size * 2, 6, 6)
grid2 = SquareGrid(Point(center.x, center.y - size / 2), size * 2, 6, 6)

for point in grid1.points.union(grid2.points):
    canvas.set_fill_color(stroke.alpha(random.random() * 1.0))
    h.draw(canvas, at_point=point, rotation=radians(90))
    canvas.set_fill_color(stroke.alpha(random.random() * 1.0))
    h.draw(canvas, at_point=point, rotation=radians(-90))

canvas.save()
