import random

from geometer import *

width = 6816
height = 5112

background, stroke = random.choice(contrast)

canvas = CoreGraphicsCanvas('output/triangles', width, height)
canvas.set_fill_color(background)
canvas.fill_background()

up_centers_grid = HorizontalHexagonGrid(canvas.center(), 120, 45, 15)
vertex_grid = HorizontalHexagonGrid(Point(canvas.center().x, canvas.center().y + (up_centers_grid.step - up_centers_grid.r)), 120, 45, 15)
down_centers_grid = HorizontalHexagonGrid(Point(canvas.center().x + (up_centers_grid.size / 2.0), canvas.center().y + up_centers_grid.r), 120, 45, 15)

for point in up_centers_grid.points:
    cls, grid = random.choice([(NorthTriangle, vertex_grid), (SouthTriangle, down_centers_grid)])
    t = cls(point, up_centers_grid.size, grid=grid)
    canvas.set_stroke_color(stroke.shade())
    fill = random.choice(fills)
    canvas.set_fill_color(fill.shade())
    t.draw(canvas)

# for point in down_centers_grid.points:
#     cls = random.choice([NorthTriangle, SouthTriangle])
#     t = cls(point, down_centers_grid.size) #, grid=vertex_grid)
#     canvas.set_stroke_color(stroke.tint())
#     fill = random.choice(fills)
#     canvas.set_fill_color(fill.shade())
#     t.draw(canvas)

canvas.save()
