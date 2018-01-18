#!/usr/bin/env python
import random
from geometer import *


stroke_widths = (0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 3.0, 4.0)


def two_edge_points(canvas):
    l = Point(0, random.random() * canvas.height)
    t = Point(random.random() * canvas.width, canvas.height)
    r = Point(canvas.width, random.random() * canvas.height)
    b = Point(random.random() * canvas.width, 0)
    
    edge_points = [l, t, r, b]
    
    return random.sample(edge_points, 2)


def draw(canvas):
    # put cool stuff here
    radius = (random.random() * canvas.width * 0.2) + (canvas.width * 0.2)
    center = canvas.random_point()
    for x in range(5):
        c = Circle(radius, center)
        c.draw(canvas)
        radius *= ((random.random() * 0.2) + 0.8)
        center = c.random_point()

    for x in range(60):
        start, end = two_edge_points(canvas)
        l = Line(start, end)
        canvas.set_stroke_width(random.choice(stroke_widths))
        
        l.draw(canvas)

    
    old_fill = canvas.fill_color
    canvas.set_fill_color(canvas.stroke_color)
    for x in range(3):        
        p = canvas.random_point()
        r = (random.random() * canvas.width * 0.25) # + (canvas.width * 0.25)
        dots = 0
    
        while dots < 200:
            c_c = canvas.random_point()
            if c_c.distance_to(p) < r:
                c = Circle(2, c_c)
                c.draw(canvas)
                dots += 1
    canvas.set_fill_color(old_fill)

