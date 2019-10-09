#!/usr/bin/env python
import random

from geometer import *


def draw(canvas):
    
    size = 64
    
    g = SquareGrid(canvas.center, size, 50, 50)
    
    for p in g.points:
        
        pair = random.choice([
            (Point(p.x - size, p.y),
             Point(p.x, p.y + size)),
            (Point(p.x, p.y + size),
             Point(p.x + size, p.y)),
            (Point(p.x + size, p.y),
             Point(p.x, p.y - size)),
            (Point(p.x, p.y - size),
             Point(p.x - size, p.y)) 
        ])
        
        terminus = random.choice([
            Point(p.x - size, p.y),
            Point(p.x, p.y + size),
            Point(p.x + size, p.y),
            Point(p.x, p.y - size)
        ])
        
        stroke = band(fills, Line.from_origin_with_slope(origin, -5/6).distance_to(p), canvas.diagonal, fuzz=True)
        canvas.set_stroke_color(stroke)
        
        
        # for terminus in pair:
        Line(p, terminus).draw(canvas)
        
