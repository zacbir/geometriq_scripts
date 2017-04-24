from geometer import *

def draw(canvas):
    
    canvas.set_stroke_width(50)
    
    t = Triangle(1024)
    
    t.draw(canvas, at_point=canvas.center)

