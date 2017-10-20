from math import radians
import random

from geometer import *

width = 2320
height = 3088

background, stroke = random.choice(contrast)

canvas = CoreGraphicsCanvas('output/trixelate-face', width, height)

reference = ReferenceImage('/Users/zac.bir/Downloads/IMG_4809.JPG', canvas)

canvas.set_fill_color(background)
canvas.fill_background()

right_grid = VerticalHexagonGrid(canvas.center, 120, 20, 20)
vertex_grid = VerticalHexagonGrid(Point(canvas.center.x + (right_grid.step - right_grid.r), canvas.center.y), 120, 24, 24)
left_grid = VerticalHexagonGrid(Point(canvas.center.x + (right_grid.size / 2.0), canvas.center.y + right_grid.r),
                                120, 20, 20)

for point in right_grid.points:
    reference_point = reference.transform_point(point)
    reference_color = reference.color_at_point(reference_point)
    canvas.set_stroke_color(stroke.shade())
    canvas.set_fill_color(reference_color.shade())

    t = EastTriangle(right_grid.size, center=point, grid=vertex_grid)
    t.draw(canvas)

for point in left_grid.points:
    reference_point = reference.transform_point(point)
    reference_color = reference.color_at_point(reference_point)
    canvas.set_stroke_color(stroke.shade())
    canvas.set_fill_color(reference_color.shade())

    t = WestTriangle(left_grid.size, center=point, grid=vertex_grid)
    t.draw(canvas)

canvas.save()
