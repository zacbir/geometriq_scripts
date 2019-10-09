#!/usr/bin/env python

import random

from geometer import *


def draw(canvas):
    #canvas.set_stroke_color(base03)
    focus = canvas.random_point()
    circles = set()
    growing = set()
    
    def is_valid(circle):
        for c in circles - {circle}:
            if circle.center.distance_to(c.center) < (circle.size + c.size):
                return False
        return True


    def gen_circle(min_r, max_r):
        r = random.randrange(min_r, max_r)
        x = random.randrange(r, canvas.width - r)
        y = random.randrange(r, canvas.height - r)
    
        return Circle(r, Point(x, y))
    
    
    def batch(num, min_r, max_r):
        for i in range(num):
            c = gen_circle(min_r, max_r)
            while not is_valid(c):
                c = gen_circle(min_r, max_r)
            circles.add(c)
            growing.add(c)


    batches = (
               (50, 128, 512),
               (150, 32, 128),
               (450, 8, 32),
               (1350, 2, 8),
               (4050, 1, 2))

    for num, min_r, max_r in batches:
        batch(num, min_r, max_r)

    while growing:
        c = growing.pop()
        while is_valid(c):
            c.size += 1

    for c in circles:
        from_focus = c.center.distance_to(focus)
        fill = band(fills, from_focus, canvas.longest_distance_from(focus), fuzz=False)
        canvas.set_stroke_color(fill.midtone())
        c.draw(canvas)

