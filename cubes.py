from math import radians
import random

from geometer import *

background, stroke = random.choice(contrast)

def draw(canvas):
    canvas.set_fill_color(background)
    canvas.fill_background()

    grid1 = VerticalHexagonGrid(canvas.center, 120, 16, 16)
    grid2 = VerticalHexagonGrid(Point(canvas.center.x - (grid1.size + grid1.r), canvas.center.y + grid1.size + grid1.r), 120, 16, 16)

    for point in grid1.points:
        h = HorizontalHexagon(grid1.step - grid1.r, center=point, grid=grid2)
        canvas.set_stroke_color(stroke.tint())
        fill = random.choice(fills)
        canvas.set_fill_color(fill.hair())
        h.draw(canvas, at_point=origin)
    
    for point in grid2.points:
        h = HorizontalHexagon(grid2.step - grid2.r, center=point, grid=grid1)
        canvas.set_stroke_color(stroke.tint())
        fill = random.choice(fills)
        canvas.set_fill_color(fill.hair())
        h.draw(canvas, at_point=origin)

