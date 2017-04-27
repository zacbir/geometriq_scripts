from geometer import *

def draw(canvas):
    canvas.set_stroke_width(1)

    t = Triangle(2048)
    
    spectrum = fills + fills[-2:0:-1]
    
    for r in range(3):
        s = Shape(0)

        p1, p2, p3 = t.points[:]
        first_point = p1
        d_x = (p2.x - p1.x) / len(spectrum)
        d_y = (p2.y - p1.y) / len(spectrum)

        for i in range(len(spectrum)):
            p_i = Point(p1.x + (i + 1) * d_x, p1.y + (i + 1) * d_y)
            s.points = [first_point, p_i, p3]
            first_point = p_i
                    
            fill = spectrum[i]
            canvas.set_fill_color(fill.alpha(1.0 / 3.0))
            s.draw(canvas, at_point=canvas.center, rotation=r * 120)

