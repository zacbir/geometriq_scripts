from geometer import *

c = CoreGraphicsCanvas('output/chunks', 4096, 4096)

def draw(canvas):
    background, stroke = base03, base1
    canvas.set_fill_color(background)
    canvas.fill_background()

    canvas.set_stroke_color(stroke)
    canvas.set_stroke_width(5)
    canvas.set_fill_color(clear)

    for i in range(72):
        s = Triangle((2 * i)**2)
        deg = i * 5
        stroke = band(fills, deg, 360)
        canvas.set_stroke_color(stroke.half())
        s.draw(canvas, at_point=canvas.center(), rotation=radians(deg))

