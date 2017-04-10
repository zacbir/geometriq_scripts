from math import floor, radians, sqrt
import random

from geometer import *

width = 4096

background, stroke = base03, base1

canvas = CoreGraphicsCanvas('output/seed_of_life', width)
canvas.set_stroke_color(stroke)
canvas.set_fill_color(background)
canvas.fill_background()

canvas.set_fill_color(clear)

size = 2048

center = canvas.center()

center_to_corner = sqrt((canvas.width / 2)**2 + (canvas.height / 2)**2)

t = Triangle(size/2)

grid1 = HorizontalHexagonGrid(center, size/2, 9, 3)

for point in grid1.points:
    t.draw(canvas, at_point=point)

t = Triangle(size)
c = Circle(t.r)

grid2 = VerticalHexagonGrid(center, t.r, 6, 6)

for point in grid2.points:
    fill_idx = int(floor((point.distance_to(center) / center_to_corner) * len(fills)))
    fill_idx = 0 if fill_idx < 0 else fill_idx
    fill_idx = -1 if fill_idx >= len(fills) else fill_idx
    fill = fills[fill_idx]
    canvas.set_fill_color(fill.hair())
    c.draw(canvas, at_point=point)

c.draw(canvas, at_point=center)

canvas.save()
