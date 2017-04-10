from math import radians
import random

from geometer import *

width = 4096
height = 4096

background, stroke = base03, base1

canvas = CoreGraphicsCanvas('output/snap_grid_test', width, height)
canvas.set_stroke_color(stroke)
canvas.set_fill_color(background)
canvas.fill_background()

canvas.set_fill_color(clear)

size = 60

up_grid = HorizontalHexagonGrid(canvas.center(), size, 9, 3)
vertex_grid = HorizontalHexagonGrid(Point(origin.x, origin.y + (up_grid.step - up_grid.r)), size, 12, 4)
down_grid = HorizontalHexagonGrid(Point(canvas.center().x + (up_grid.size / 2.0), canvas.center().y + up_grid.r),
                                  size, 9, 3)

for point in up_grid.points:
    # canvas.set_stroke_color(stroke.tint())
    # fill = random.choice(fills)
    # canvas.set_fill_color(fill.shade())

    t = Triangle(up_grid.size, center=point, grid=vertex_grid)
    t.draw(canvas, at_point=origin)

for point in down_grid.points:
    # canvas.set_stroke_color(stroke.tint())
    # fill = random.choice(fills)
    # canvas.set_fill_color(fill.shade())

    t = Triangle(down_grid.size, center=origin, grid=vertex_grid)
    t.draw(canvas, at_point=point, rotation=radians(180))

canvas.save()
