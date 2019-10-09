#!/usr/bin/env python

from geometer import *


def draw(canvas):
    
    cp = Point(canvas.width / 2, canvas.height)
    canvas.set_stroke_width(8)
    
    vert_pairs = [
        (Point(0, y), Point(canvas.width, y))
        for y in range(canvas.height, -1 * canvas.height, -128)]
    horz_pairs = [
        (Point(x, 0), Point(canvas.width - x, 0))
        for x in range(0, int(canvas.width / 2), 128)]
    
    pairs = vert_pairs + horz_pairs
    
    for i, pair in enumerate(vert_pairs):
        
        color = band(fills, i, len(vert_pairs)).half()
        canvas.set_stroke_color(color)
        
        Curve(pair, [cp]).draw(canvas)

