import random

from geometer import *

def draw(canvas):
    
    for c in range(6):
       
        p = canvas.random_point() 
        r = random.random() * 1024
        a = random.random() * 120
        
        fills = random.choice([(magenta, red, orage), (red, orange, yellow), (orange, yellow, green), (yellow, green, cyan), (green, cyan, blue), (cyan, blue, violet), (blue, violet, magenta)])
        
        for s in range(3):
            canvas.set_fill_color(fills[s].half())
            cs = CircleSegment(r, 120)
            
            cs.draw(canvas, at_point=p, rotation=s * 120 + a)

