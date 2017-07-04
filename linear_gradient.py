from geometer import *

def draw(canvas):
    canvas.set_fill_color(clear)

    line = Line(canvas.random_point(), center=canvas.random_point())
    
    max_length = max([line.distance_to(p) for p in canvas.corners])

    gradient = list(green.gradient_to(red, 32))
    thickness = range(1, 32)

    grid = HorizontalHexagonGrid(canvas.center, 128, 45, 15)

    for p in grid.linear_sort(line):
        stroke = band(gradient, line.distance_to(p), max_length)
        weight = band(thickness, line.distance_to(p), max_length)
        canvas.set_stroke_color(stroke.half())
        canvas.set_stroke_width(weight)
        c = Circle(128)
        c.draw(canvas, at_point=p)
