import random

from geometer import *

width = 4096
height = 4096

background, stroke = random.choice(contrast)

canvas = CoreGraphicsCanvas('output/cubes', width, height)
canvas.set_fill_color(background)
canvas.fill_background()

grid1 = VerticalHexagonGrid(canvas.center, 120, 30, 30)
grid1_vertices = VerticalHexagonGrid(grid1.start, 120, 32, 32)
grid2 = VerticalHexagonGrid(Point(canvas.center.x, canvas.center.y + grid1.size), 120, 30, 32)
grid2_vertices = VerticalHexagonGrid(grid2.start, 120, 32, 34)

for point in grid1.points:
    h = VerticalHexagon(point, grid1.size, grid=grid1_vertices)
    canvas.set_stroke_color(stroke.tint())
    fill = random.choice(fills)
    canvas.set_fill_color(fill)
    h.draw(canvas)

for point in grid2.points:
    h = VerticalHexagon(point, grid2.size, grid=grid2_vertices)
    canvas.set_stroke_color(stroke.tint())
    fill = random.choice(fills)
    canvas.set_fill_color(fill)
    h.draw(canvas)

canvas.save()
