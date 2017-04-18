from math import radians

from geometer import *

def draw(canvas):
    background, stroke = base03, base1
    canvas.set_fill_color(background)
    canvas.set_stroke_color(stroke)
    canvas.fill_background()
    
    canvas.set_fill_color(clear)
    
    c = Circle(500)
    c.draw(canvas, at_point=canvas.center)
    
    t = Triangle(3000)
    t.draw(canvas, at_point=Point(canvas.center.x - 500, canvas.center.y))
    t.draw(canvas, at_point=Point(canvas.center.x + 500, canvas.center.y), rotation=radians(180))

