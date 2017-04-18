from math import floor, radians
import random

from geometer import *

c = CoreGraphicsCanvas('output/arcs', 4096, 4096)

background, stroke = random.choice(contrast)

def draw(canvas):
    canvas.set_fill_color(background)
    canvas.set_stroke_color(stroke)

    canvas.fill_background()

    canvas.set_fill_color(clear)

    for d in range(200):
        radius = d * 25
        color_index = int(floor(radius / (canvas.center.distance_to(Point(c.width, c.height))) * len(fills)))
        color_index = 0 if color_index < 0 else color_index
        color_index = -1 if color_index >= len(fills) else color_index
        canvas.set_stroke_color(fills[color_index].tint())
        canvas.set_stroke_width(random.random() * 10)
        a = Arc(d * 25, random.random() * 120 + 180)
        a.draw(canvas, at_point=c.center, rotation=radians(random.random() * 360))

