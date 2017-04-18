import random

from geometer import *

def draw(canvas):
    canvas.set_fill_color(clear)

    for d in range(20):
        radius = d * 100
        rotate_angle = random.random() * 60
        canvas.set_stroke_width(50)
        canvas.set_stroke_color(base1)
        qc = QuarterCircle(radius)
        qc.draw(canvas, at_point=canvas.center, rotation=rotate_angle)
        qc.draw(canvas, at_point=canvas.center, rotation=rotate_angle + 180)
        canvas.set_stroke_color(red)
        qc.draw(canvas, at_point=canvas.center, rotation=rotate_angle+ 90)
        qc.draw(canvas, at_point=canvas.center, rotation=rotate_angle + 270)
