#!/usr/bin/env python

from math import cos, pi, sin
import random

from geometriq import *


class StopPackingException(Exception):
    pass


def draw(canvas):
    canvas.set_stroke_color(base03)
    focus = canvas.random_point()
    bound_circle = Circle(canvas.width * 0.45, canvas.center)
    max_r = min(canvas.height, canvas.width) * 0.2
    min_r = max_r * 0.5
    circles = set()
    
    def is_valid(circle):
        if (circle.center.distance_to(bound_circle.center) + circle.size) > bound_circle.size:
            return False
        
        if circle.size > max_r:
            return False

        for c in circles - {circle}:
            if circle.center.distance_to(c.center) < (circle.size + c.size):
                return False

        return True


    def gen_circle():
        angle = random.random() * 2 * pi
        x = canvas.center.x + random.random() * bound_circle.size * cos(angle)
        y = canvas.center.y + random.random() * bound_circle.size * sin(angle)
    
        return Circle(min_r, Point(x, y))
    
    
    try:
        while True:
            c = gen_circle()
            attempts = 0
            while not is_valid(c):
                c = gen_circle()
                attempts += 1
                if attempts > 100:
                    min_r = max(0.5 * min_r, 1)
                if attempts > 1000:
                    print(f"Reached maximum packing with {len(circles)} circles. Quitting.")
                    raise StopPackingException
            circles.add(c)
            while is_valid(c):
                c.size += 1
            # no longer valid, might as well draw it.
            from_focus = c.center.distance_to(focus)
            fill = band(fills, from_focus, canvas.longest_distance_from(focus), fuzz=False)
            canvas.set_fill_color(fill.midtone())
            c.draw(canvas)

            min_r = c.size * 0.5
            if len(circles) % 200 == 0:
                print(f"Added 200 circles to our collection of {len(circles)} circles.")
    except StopPackingException:
        print(f"Finished packing our {len(circles)} circles.")

