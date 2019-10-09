#!/usr/bin/env python
import random

from geometer import *


def draw(canvas):
    
    size = 64

    north = lambda point: Point(point.x, point.y + size)
    east = lambda point: Point(point.x + size, point.y)
    south = lambda point: Point(point.x, point.y - size)
    west = lambda point: Point(point.x - size, point.y)
    
    used = {}
    
    g = SquareGrid(canvas.center, size, 25, 25)
    
    ref_line = Line.from_origin_with_slope(Point(canvas.width, 0), 2/3)
    
    for p in g.points:
        
        stroke = band(fills, ref_line.distance_to(p), canvas.diagonal, fuzz=True)
        canvas.set_stroke_color(stroke)
        
        num_used = used.setdefault(p, 0)
        if num_used == 2:
            continue
        
        candidates = [
            g.closest_point_to(func(p)) for func in [north, east, south, west]]
        
        random.shuffle(candidates)
        
        while num_used <= 2 and len(candidates):
            candidate = candidates.pop()
            num_candidate_used = used.setdefault(candidate, 0)
            if num_candidate_used == 2:
                continue
            num_used += 1
            num_candidate_used += 1
            used[candidate] = num_candidate_used
            Line(p, candidate).draw(canvas)
        
        used[p] = num_used

