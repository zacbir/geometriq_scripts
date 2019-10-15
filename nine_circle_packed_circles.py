#!/usr/bin/env python

from math import cos, pi, sin
import random

from geometriq import *


class StopPackingException(Exception):
    pass


def draw(canvas):

    colors = [[magenta, red, orange],
              [violet, base3, yellow],
              [blue, cyan, green]]
    
    canvas.set_stroke_color(base03)

    chunk_width = (canvas.width / 3)
    chunk_height = (canvas.height / 3)
    smaller_side = min(chunk_width, chunk_height)

    for x in range(3):
        for y in range(3):

            chunk_x_zero = (x / 3) * canvas.width
            chunk_y_zero = (y / 3) * canvas.height
            chunk_x_max = chunk_x_zero + chunk_width
            chunk_y_max = chunk_y_zero + chunk_height

            chunk_center = Point((chunk_x_max + chunk_x_zero) / 2, (chunk_y_max + chunk_y_zero) / 2)

            bound_circle = Circle(smaller_side * 0.45, chunk_center)
            print(f"Bound circle: {bound_circle}")
            max_r = min(chunk_height, chunk_width) * 0.2
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
                x = chunk_center.x + random.random() * bound_circle.size * cos(angle)
                y = chunk_center.y + random.random() * bound_circle.size * sin(angle)
        
                return Circle(min_r, Point(x, y))
    
    
            try:
                while True:
                    c = gen_circle()
                    attempts = 0
                    while not is_valid(c):
                        c = gen_circle()
                        attempts += 1
                        if attempts > 1000:
                            print(f"Reached maximum packing with {len(circles)} circles. Quitting.")
                            raise StopPackingException
                    circles.add(c)
                    while is_valid(c):
                        c.size += 1
                        # no longer valid, might as well draw it.
                        # from_focus = c.center.distance_to(focus)
                        fill = colors[x][y]
                        # fill = band(fills, from_focus, canvas.longest_distance_from(focus), fuzz=False)
                        canvas.set_fill_color(fill.midtone())
                        c.draw(canvas)

                    min_r = c.size * 0.5
                    if len(circles) % 200 == 0:
                        print(f"Added 200 circles to our collection of {len(circles)} circles.")
            except StopPackingException:
                print(f"Finished packing our {len(circles)} circles.")

