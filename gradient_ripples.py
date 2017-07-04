from geometer import *

def draw(canvas):
    canvas.set_fill_color(clear)
    epicenter = canvas.random_point()
    max_length = canvas.longest_distance_from(epicenter)

    gradient = list(green.gradient_to(red, 32))
    thickness = range(1, 32)

    grid = HorizontalHexagonGrid(canvas.center, 128, 45, 15)

    for p in grid.radial_sort(epicenter):
        stroke = band(gradient, p.distance_to(epicenter), max_length)
        weight = band(thickness, p.distance_to(epicenter), max_length)
        canvas.set_stroke_color(stroke.half())
        canvas.set_stroke_width(weight)
        c = Circle(128)
        c.draw(canvas, at_point=p)
