import math
import random

from geometer import *

def angle_from(point, to=origin):
    if point.x == to.x:
        if point.y >= to.y:
            return 90
        else:
            return 270
    if point.y == to.y:
        if point.x >= to.x:
            return 360
        else:
            return 180
    base_degrees = math.degrees(math.asin((point.x - to.x) / float(point.distance_to(to))))
    
    if point.x > to.x:
        if point.y > to.y:
            base_degrees += 0
        else:
            base_degrees += 270
    else:
        if point.y > to.y:
            base_degrees += 90
        else:
            base_degrees += 180
    
    return base_degrees

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
        
        d = angle_from(p, to=canvas.center)
        fill_idx = d
        fill_skew = random.random()
        if fill_skew <= 0.25:
            fill_idx = 338 if fill_idx < 22 else fill_idx - 22
        if fill_skew >= 0.75:
            fill_idx = 22 if fill_idx > 338 else fill_idx + 22
        fill = band(fills, fill_idx, 360)        
 
        rotation_d = random.random() * 180       

        c = Square(96)
        canvas.set_fill_color(base03)
        c.draw(canvas, at_point=p, rotation=rotation_d)            
        canvas.set_fill_color(fill.tint())
        c.draw(canvas, at_point=p, rotation=rotation_d)
        count += 1
