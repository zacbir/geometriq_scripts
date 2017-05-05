from math import pi
import random

from geometer import *

def draw(canvas):
    canvas.set_fill_color(clear)
    radius_incr = 250

    def angle_for_gap(gap, radius):
        circumference = 2 * pi * radius
        return 360 * (circumference - gap) / circumference
    
    for i in range(8):
        
        radius = radius_incr * i + radius_incr
        
        start_angle = random.random() * 360
        
        a = Arc(radius, angle_for_gap(radius_incr, radius))
        
        a.draw(canvas, at_point=canvas.center, rotation=start_angle)
        
        Line(to_point=Point(radius + radius_incr, 0), center=Point(radius, 0)).draw(canvas, at_point=canvas.center, rotation=start_angle)
        
