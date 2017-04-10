from math import radians
import random

from geometer import *

width = 4096
height = 4096

background, stroke = base03, base1

canvas = CoreGraphicsCanvas('output/circle_segments', width, height)
canvas.set_stroke_color(stroke)
canvas.set_fill_color(background)
canvas.fill_background()

center = canvas.center()

size = 128

grid1 = SquareGrid(Point(center.x, center.y + size / 2), size * 2.25, 7, 7)

min_point = min(grid1.points)
max_point = max(grid1.points)

total_grid_width = max_point.x - min_point.x
total_grid_height = max_point.y - min_point.y

for point in grid1.points:
    canvas.set_stroke_color(base00.hair())
    canvas.draw_line(Point(min_point.x, point.y), Point(max_point.x, point.y))
    canvas.draw_line(Point(point.x, min_point.y), Point(point.x, max_point.y))

for point in grid1.points:
    alpha = (point.x - min_point.x) / total_grid_width
    angle = ((point.y - min_point.y) / total_grid_height) * 360
    rotation = random.random() * 360

    canvas.set_stroke_color(stroke)
    canvas.set_fill_color(base1.alpha(alpha))
    segment = CircleSegment(size, angle=angle)
    segment.draw(canvas, at_point=point, rotation=radians(rotation))

canvas.save()
