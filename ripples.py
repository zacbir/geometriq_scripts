from math import sqrt

from geometer import *

def draw(canvas):
    
    t = Triangle(2048, center=canvas.center)
    strokes = (red, green, blue)
    band_max = sqrt((canvas.width / 2)**2 + (canvas.height / 2)**2)
    
    weights = [x for x in range(100)]
    opacities = [x / 255 for x in range(256)]
    
    canvas.set_fill_color(clear)
    
    bands = 50

    for j in range(bands):   
        for i, p in enumerate(t.points):
            color = strokes[i]
            opacity = band(opacities, j, bands)
            weight = band(weights, j, bands)
            
            canvas.set_stroke_width(weight)
            canvas.set_stroke_color(color.alpha(1 - opacity))
            
            c = Circle(100 * j, center=p)
            c.draw(canvas, at_point=origin)
   
