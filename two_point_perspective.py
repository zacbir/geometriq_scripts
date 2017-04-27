import math
import random

from geometer import *

def draw(canvas):
    
    canvas.set_stroke_width(0.5)
    x_offset = canvas.width / 20
    y_offset = canvas.height / 20
    p1 = Point(x_offset, canvas.center.y)
    p2 = Point(canvas.width - x_offset, canvas.center.y)
    
    vertical_line_x = random.random() * canvas.width / 3.0 + canvas.width / 3.0
    
    sheets = 17
    
    for i in range(sheets):
        canvas.set_stroke_color(base1.half())
        y = ((canvas.height - (2 * y_offset)) / sheets) * i + y_offset
        s = Shape(0)

        s_p1 = Point(vertical_line_x, y)

        line1 = Line(center=s_p1, to_point=p1)
        line1.draw(canvas)        
        s_p2 = line1.midpoint()
        
        line2 = Line(center=s_p1, to_point=p2)
        line2.draw(canvas)
        s_p4 = line2.midpoint()

        line3 = Line(center=s_p2, to_point=p2)
        line3.draw(canvas)
        line4 = Line(center=s_p4, to_point=p1)
        line4.draw(canvas)
        s_p3 = line3.intersection_with(line4)

        s.points = [s_p1, s_p2, s_p3, s_p4]

        fill = band(fills, i, sheets)
        canvas.set_fill_color(fill.half())
        canvas.set_stroke_color(clear)
        
        s.draw(canvas)

