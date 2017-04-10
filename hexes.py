import random

from geometer import *

width = 6816
height = 5112

background, stroke = random.choice(contrast)

grey_band = 255.0 / 6.0
greys = [Color.from_full_value(x * grey_band, x * grey_band, x * grey_band) for x in xrange(7)]

canvas = CoreGraphicsCanvas('output/triangles', width, height)
# reference = ReferenceImage('/Users/zbir/Downloads/apple-logo-black.png', canvas)
canvas.set_fill_color(background)
canvas.fill_background()

up_centers_grid = VerticalHexagonGrid(canvas.center(), 120, 15, 15)# vertex_grid = HorizontalHexagonGrid(Point(canvas.center().x, canvas.center().y + (up_centers_grid.step - up_centers_grid.r)), 120, 6, 2)
vertex_grid = HorizontalHexagonGrid(canvas.center(), (up_centers_grid.step - up_centers_grid.r), 45, 45)

for point in up_centers_grid.points:
    canvas.set_stroke_color(random.choice(strokes).tint())
    canvas.set_fill_color(random.choice(fills).shade())

    t = HorizontalHexagon(point, (up_centers_grid.step - up_centers_grid.r), grid=vertex_grid)
    t.draw(canvas)
    # t2 = VerticalHexagon(point, (up_centers_grid.step - up_centers_grid.r))
    # canvas.set_stroke_color(blue.hair())
    # t2.draw(canvas)

# for point in vertex_grid.points:
#     canvas.set_stroke_color(blue.hair())
#     shape = Circle(point, 2)
#     shape.draw(canvas)

# for point in down_centers_grid.points:
#     canvas.set_stroke_color(green)
#     shape = Circle(point, 2)
#     shape.draw(canvas)
#
#     t = SouthTriangle(point, down_centers_grid.size) #, grid=vertex_grid)
#     canvas.set_stroke_color(blue.half())
#     t.draw(canvas)


canvas.save()
