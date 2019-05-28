#!/usr/bin/env python

from geometer import *


def draw(canvas):
    
    v_cps = [
        Point(canvas.width / 2, 0),
        Point(canvas.width / 2, canvas.height)]
    h_cps = [
        Point(0, canvas.height / 2),
        Point(canvas.width, canvas.height / 2)]
    
    canvas.set_stroke_width(8)
    
    vert_pairs = [
        (Point(0, y), Point(canvas.width, y))
        for y in range(0, canvas.height + 128, 128)]
    horz_pairs = [
        (Point(x, 0), Point(x, canvas.height))
        for x in range(0, canvas.width + 128, 128)]

    def draw_pairs(pairs, cp):
        for i, pair in enumerate(pairs):
            color = band(list(reversed(fills)), i, len(pairs)).half()
            canvas.set_stroke_color(color)

            Curve(pair, [cp]).draw(canvas)
                      
    for pair_set, cps in ((vert_pairs, v_cps), (horz_pairs, h_cps)):    
        draw_pairs(pair_set, cps[0])
        
        draw_pairs(list(reversed(pair_set)), cps[1])

