from math import radians, tan
import random
from geometer import *


def draw(canvas):

    size = 256
    
    up_grid = HorizontalHexagonGrid(canvas.center, size, 20, 5)
    vertex_grid = HorizontalHexagonGrid(Point(canvas.center.x, canvas.center.y + (up_grid.step - up_grid.r)), size, 24, 24)
    down_grid = HorizontalHexagonGrid(Point(canvas.center.x + up_grid.size, canvas.center.y + (up_grid.step + up_grid.r)), size, 22, 6)

    center_triangle = NorthTriangle(size, canvas.center, grid=vertex_grid)

    test_line = Line.from_origin_with_slope(center_triangle.points[1], tan(radians(60)))

    greys = [base02, base01, base00, base0, base1, base2]

    def fill_triangle(cls, center):
        t = cls(size, center, grid=vertex_grid)

        left = test_line.compare(center)
        alpha = (random.random() * 0.2) + 0.8
        bottom_stroke = clear

        if left < 0:
            top_stroke = base02
            top_fill = base03
            bottom_fill = base3
        else:
            top_stroke = base2
            top_fill = base3
            bottom_fill = base03

        # chance that we might fill with a random intermediate
        if (center.distance_to(canvas.center) < (canvas.width / 2.5)) and (random.random() < 0.85):
            top_stroke = clear
            top_fill = band(fills, p.x, canvas.width, fuzz=True)
            bottom_fill = random.choice(greys)
            alpha = (random.random() * 0.5) + 0.25

        canvas.set_stroke_color(bottom_stroke)
        canvas.set_fill_color(bottom_fill)
        t.draw(canvas)
        
        canvas.set_stroke_color(top_stroke.alpha(alpha))
        canvas.set_fill_color(top_fill.alpha(alpha))
        t.draw(canvas)

    for p in up_grid.points:
        fill_triangle(NorthTriangle, p)
    
    for p in down_grid.points:
        fill_triangle(SouthTriangle, p)
