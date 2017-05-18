import random

from geometer import *

def draw(canvas):
    
    strokes = [red, orange, yellow, green, blue, violet]
    
    circles = 60
    
    for i in range(circles):
        
        c = Circle(1000, center=Point(50 * i, 0))
        
        for t in range(18):
            
            stroke = strokes[t % len(strokes)]
            canvas.set_stroke_color(stroke.alpha(1 - 2 * float(i) / circles))
            c.draw(canvas, at_point=canvas.center, rotation=t * 20 + 0.6 * i)

