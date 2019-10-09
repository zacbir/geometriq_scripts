from math import radians, tan
import random
from geometer import *


def draw(canvas):

    size = 256
    
    up_grid = HorizontalHexagonGrid(canvas.center, size, 20, 5)
    vertex_grid = HorizontalHexagonGrid(Point(canvas.center.x, canvas.center.y + (up_grid.step - up_grid.r)), size, 24, 24)
    down_grid = HorizontalHexagonGrid(Point(canvas.center.x + up_grid.size, canvas.center.y + (up_grid.step + up_grid.r)), size, 22, 6)

    canvas.set_stroke_color(base02)

    def fill_triangle(cls, center):
        t = cls(size, center, grid=vertex_grid)

        # chance that we might fill with a random intermediate
        if random.random() < 0.9:
            fill = band(fills, p.y, canvas.height, fuzz=True)
            canvas.set_fill_color(fill.midtone())
            t.draw(canvas)

    for p in up_grid.points:
        fill_triangle(NorthTriangle, p)
    
    for p in down_grid.points:
        fill_triangle(SouthTriangle, p)
