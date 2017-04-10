from math import radians
import random

from geometer import *

width = 3024
height = 4032

background, stroke = random.choice(contrast)

canvas = CoreGraphicsCanvas('output/trixelate', width, height)

reference = ReferenceImage('/Users/zbir/Downloads/IMG_2417.JPG', canvas)

canvas.set_fill_color(background)
canvas.fill_background()

up_grid = HorizontalHexagonGrid(canvas.center(), 30, 240, 80)
vertex_grid = HorizontalHexagonGrid(Point(origin.x, origin.y + (up_grid.step - up_grid.r)), 30.5, 3, 1)
down_grid = HorizontalHexagonGrid(Point(canvas.center().x + (up_grid.size / 2.0), canvas.center().y + up_grid.r),
                                  30, 240, 80)

for point in up_grid.points:
    reference_point = reference.transform_point(point)
    reference_color = reference.color_at_point(reference_point)
    canvas.set_stroke_color(stroke.shade())
    canvas.set_fill_color(reference_color.shade())

    t = Triangle(up_grid.size, grid=vertex_grid)
    t.draw(canvas, at_point=point)

for point in down_grid.points:
    reference_point = reference.transform_point(point)
    reference_color = reference.color_at_point(reference_point)
    canvas.set_stroke_color(stroke.shade())
    canvas.set_fill_color(reference_color.shade())

    t = Triangle(down_grid.size, grid=vertex_grid)
    t.draw(canvas, at_point=point, rotation=radians(180))

canvas.save()
