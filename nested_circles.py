from geometer import *

def draw(canvas):
    
    canvas.set_stroke_width(4)
    canvas.set_stroke_color(base1)
    canvas.set_fill_color(base03)
    
    canvas.fill_background()
    
    for i in range(20):
        size = 1500 / (i + 1)
        c = Circle(size)
        center = Point(canvas.center.x, canvas.center.y + i * size)
        c.draw(canvas, at_point=center)

