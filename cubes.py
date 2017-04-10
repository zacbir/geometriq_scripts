from math import floor
import random

from geometer import *

width = 4096
height = 4096

canvas = CoreGraphicsCanvas('output/cubes', width, height)
canvas.set_stroke_color(base1)
canvas.set_fill_color(base03)
canvas.fill_background()

grid1 = HorizontalHexagonGrid(canvas.center(), 120, 12, 4)
grid2 = HorizontalHexagonGrid(Point(canvas.center().x, canvas.center().y - (grid1.step - grid1.r)), 120, 12, 4)

shared_vertices = HorizontalHexagonGrid(Point(canvas.center().x, canvas.center().y + (grid1.step - grid1.r)), 120, 15, 5)

grid1_vertices = Grid(grid1.start, grid1.size, 0, 0)
grid1_vertices.points = grid1.points.union(shared_vertices.points)

grid2_vertices = Grid(grid2.start, grid2.size, 0, 0)
grid2_vertices.points = grid2.points.union(shared_vertices.points)

total_grid_points = grid1_vertices.points.union(grid2_vertices.points)

min_x = min((p.x for p in total_grid_points))
max_x = max((p.x for p in total_grid_points))

total_grid_width = max_x - min_x  # 100

for point in grid1.points:
    percentile = float(point.x - min_x) / float(total_grid_width)
    band = int(floor(percentile * len(fills)))
    try:
        fill = fills[band]
    except IndexError:
        fill = fills[-1]

    try:
        stroke = fills[-1 * band]
    except IndexError:
        stroke = fills[0]

    h = VerticalHexagon(point, grid1.step - grid1.r, grid=grid2_vertices)
    # fill = random.choice([red, green, blue])
    canvas.set_stroke_color(stroke.tint())
    canvas.set_fill_color(fill.shade())
    h.draw(canvas)

for point in grid2.points:
    percentile = float(point.x - min_x) / float(total_grid_width)
    band = int(floor(percentile * len(fills)))
    try:
        fill = fills[band]
    except IndexError:
        fill = fills[-1]

    try:
        stroke = fills[-1 * band]
    except IndexError:
        stroke = fills[0]

    h = VerticalHexagon(point, grid2.step - grid2.r, grid=grid1_vertices)
    # fill = random.choice([red, green, blue])
    canvas.set_stroke_color(stroke.tint())
    canvas.set_fill_color(fill.shade())
    h.draw(canvas)

canvas.save()
