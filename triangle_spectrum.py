from geometer import *

def draw(canvas):
    canvas.set_stroke_width(1)

    t = Triangle(2048)
    
    #t.draw(canvas)
    
    for r in range(3):
        s = Shape(0)

        p1, p2, p3 = t.points[:]
        first_point = p1
        d_x = (p2.x - p1.x) / 8.0
        d_y = (p2.y - p1.y) / 8.0

        for i in range(8):
            p_i = Point(p1.x + (i + 1) * d_x, p1.y + (i + 1) * d_y)
            s.points = [first_point, p_i, p3]
            first_point = p_i
                    
            fill = fills[i]
            canvas.set_fill_color(fill.alpha(1.0 / 3.0))
            s.draw(canvas, at_point=canvas.center, rotation=r * 120)

