from math import sqrt

from geometer import *

def draw(canvas):
    
    h = Hexagon(1024, center=canvas.center)
    strokes = (red, green, blue, yellow, cyan, magenta)
    
    weights = [x for x in range(50)]
    opacities = [x / 255 for x in range(256)]
    
    canvas.set_fill_color(clear)
    
    bands = 25

    for j in range(bands):   
        for i, p in enumerate(h.points):
            color = strokes[i]
            opacity = band(opacities, j, bands)
            weight = band(weights, j, bands)
            
            canvas.set_stroke_width(weight)
            canvas.set_stroke_color(color.alpha(1 - opacity))
            
            c = Circle(75 * j, center=p)
            c.draw(canvas, at_point=origin)
   
