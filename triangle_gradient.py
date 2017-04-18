from geometer import *

def draw(canvas):
    
    canvas.set_stroke_color(base1)
    canvas.set_fill_color(base03)
    canvas.fill_background()
    
    size = 240
    
    grid = HorizontalHexagonGrid(canvas.center, size, 18, 6)
    vertex_grid = HorizontalHexagonGrid(Point(canvas.center.x, canvas.center.y + (grid.step - grid.r)), size, 21, 7)
    
    max_y = max(grid.points).y
    min_y = min(grid.points).y
    
    for p in grid.points:
        t = Triangle(size, center=p, grid=vertex_grid)
        weight = band(range(150), p.y, max_y, min_y)
        canvas.set_stroke_width(weight)
        t.draw(canvas, at_point=origin)

