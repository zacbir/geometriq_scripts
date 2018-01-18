from geometer import *


def draw(canvas):
    size = canvas.width / 2 * 0.8
    canvas.set_stroke_color(clear)
    # canvas.set_stroke_width(2.0)
    steps = 96

    for i in range(steps):
        h = Hexagon(size)
        size = size * 0.95
        canvas.set_fill_color(base03.alpha(0.65))
        h.draw(canvas, canvas.center, 5.625 * i * -1)
        canvas.set_fill_color(fills[i % len(fills)].alpha(0.35))
        h.draw(canvas, canvas.center, 5.625 * i)
