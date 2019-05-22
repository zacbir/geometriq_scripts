#!/usr/bin/env python
import random

from geometer import *


def draw(canvas):
    
    r = Rectangle(center=origin, to_point=Point(900, 400))
    
    for i in range(128):
        
        factor = random.random() * 4
        p = canvas.random_point()
        
        c = band(fills, p.x * factor, canvas.width, fuzz=True)

        canvas.set_stroke_color(c)
        canvas.set_fill_color(c.midtone())
        
        r.draw(canvas, at_point=p, scale_x=factor, scale_y=factor)

