import random

from geometer import *


def draw(canvas):
    
    canvas.set_stroke_width(random.random() * 0.4 + 0.1)
    x_offset = canvas.width / 20
    y_offset = canvas.height / 20
    p1 = Point(x_offset, canvas.center.y)
    p2 = Point(canvas.width - x_offset, canvas.center.y)
    
    x = random.random() * canvas.width / 3.0

    line1_ratio = random.random() * 0.8
    line2_ratio = random.random() * 0.8

    sheets = 16

    for i in range(sheets):
        canvas.set_stroke_color(base1.alpha(random.random() * 0.5 + 0.25))
        x += 100
        y = (canvas.height / sheets) * i + y_offset
        s = Shape(0)

        s_p1 = Point(x, y)

        line1 = Line(center=s_p1, to_point=p1)
        line1.extended().draw(canvas)
        s_p2 = line1.point_from_center(line1.length * line1_ratio)
        
        line2 = Line(center=s_p1, to_point=p2)
        line2.extended().draw(canvas)
        s_p4 = line2.point_from_center(line2.length * line2_ratio)

        line3 = Line(center=s_p2, to_point=p2)
        line3.extended().draw(canvas)
        line4 = Line(center=s_p4, to_point=p1)
        line4.extended().draw(canvas)
        s_p3 = line3.intersection_with(line4)

        s.points = [s_p1, s_p2, s_p3, s_p4]

        fill = band(fills, i, sheets)
        canvas.set_fill_color(fill.half())
        canvas.set_stroke_color(clear)
        
        s.draw(canvas)

