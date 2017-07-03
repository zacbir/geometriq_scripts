from geometer import *

initial_size = 1024
scale = 0.5
max_iterations = 5

def hex_at(canvas, point, size, it):
    if it >= max_iterations:
        return
    h = VerticalHexagon(size, point)
    for p in h.points:
        stroke = band(fills, it, max_iterations)
        c = HorizontalHexagon(size, p)
        canvas.set_stroke_color(stroke.shade())
        c.draw(canvas)
        hex_at(canvas, p, size * scale, it + 1)

def draw(canvas):
    
    canvas.set_fill_color(clear)
    
    hex_at(canvas, canvas.center, initial_size, 0)

