from geometer import *


def draw(canvas):

    canvas.set_stroke_width(16)

    t = SouthTriangle(2048)
    t.draw(canvas, at_point=canvas.center)
