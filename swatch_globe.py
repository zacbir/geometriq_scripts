import math
import random

from geometer import *

def draw(canvas):
    # canvas.set_fill_color(base3)
    # canvas.fill_background()
    canvas.set_stroke_color(clear)
    max_distance = 1536
    band_width = max_distance / len(fills)
    
    count = 0
    
    while count < 8192:
        p = canvas.random_point()
        while p.distance_to(canvas.center) > max_distance:
            p = canvas.random_point()
        
        fill_idx = p.distance_to(canvas.center)
        fill_skew = random.random()
        if fill_skew <= 0.25:
            fill_idx = 0 if fill_idx < band_width else fill_idx - band_width
        if fill_skew >= 0.75:
            fill_idx = max_distance if fill_idx > (max_distance - band_width) else  fill_idx + band_width
        fill = band(fills, fill_idx, max_distance) 
        
 
        rotation_d = random.random() * 180       

        c = Square(96)
        canvas.set_fill_color(base03)
        c.draw(canvas, at_point=p, rotation=rotation_d)            
        canvas.set_fill_color(fill.tint())
        c.draw(canvas, at_point=p, rotation=rotation_d)
        count += 1
