#!/usr/bin/env python
import random

from geometer import *


def draw(canvas):
    
    size = 256

    north = lambda point: Point(point.x, point.y + size),
    east = lambda point: Point(point.x + size, point.y),
    south = lambda point: Point(point.x, point.y - size),
    west = lambda point: Point(point.x - size, point.y)
    
    used = {}
    
    g = SquareGrid(canvas.center, 256, 5, 5)
    
    for p in g.points:
        
        # check to see if we've seen two already
        
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

