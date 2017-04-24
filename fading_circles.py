from math import sqrt
import random

from geometer import *

def draw(canvas):
    
    weights = [i + 1 for i in range(60)]
    opacities = [i / 255 for i in range(256)]
    
    g = HorizontalHexagonGrid(canvas.center, 150, 30, 10)
    band_max = sqrt((canvas.width / 2)**2 + (canvas.height / 2)**2)
    
    canvas.set_fill_color(clear)
    
    reversed_fills = list(reversed(fills))
    
    for p in g.points:
        
        distance_to_center = p.distance_to(canvas.center)
        weight = band(weights, distance_to_center, band_max)
        opacity = 1 - band(opacities, distance_to_center, band_max)
        color = band(reversed_fills, distance_to_center, band_max)
        canvas.set_stroke_width(weight)
        canvas.set_stroke_color(color.alpha(opacity))
        c = Circle(120)
        c.draw(canvas, at_point=p)

