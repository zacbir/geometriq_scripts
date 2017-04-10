from math import radians
import random

from geometer import *

width = 4096
height = 4096

background, stroke = base03, base1

canvas = CoreGraphicsCanvas('output/rhombus_test', width, height)
canvas.set_stroke_color(stroke)
canvas.set_fill_color(background)
canvas.fill_background()

canvas.set_fill_color(clear)

size = 240

up_grid = HorizontalHexagonGrid(canvas.center(), size, 9, 3)
vertex_grid = VerticalHexagonGrid(Point(origin.x + (up_grid.step - up_grid.r), origin.y), size + 0.5, 3, 1)

for point in up_grid.points:
    # canvas.set_stroke_color(stroke.tint())
    # fill = random.choice(fills)
    # canvas.set_fill_color(fill.shade())

    t = HexagonalRhombus(up_grid.step - up_grid.r, grid=vertex_grid)
    canvas.set_fill_color(red.shade())
    t.draw(canvas, at_point=point, rotation=radians(0))
    canvas.set_fill_color(green.shade())
    t.draw(canvas, at_point=point, rotation=radians(120))
    canvas.set_fill_color(blue.shade())
    t.draw(canvas, at_point=point, rotation=radians(240))

canvas.save()
