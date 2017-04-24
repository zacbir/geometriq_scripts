from geometer import *

def draw(canvas):
    
    canvas.set_fill_color(clear)
    
    s = Square(canvas.width, center=canvas.center)
    weights = [x for x in range(128, 1, -1)]
    opacities = [x / 255 for x in range(256)]
    
    for corner in s.points:
        steps = 16
        for i in range(steps):
            radius = (i + 1) * ((canvas.width / 2) / steps)
            canvas.set_stroke_width(band(weights, i, steps))
            canvas.set_stroke_color(base1.alpha(band(opacities, i, steps)))
            c = Circle(radius)
            c.draw(canvas, at_point=corner)

