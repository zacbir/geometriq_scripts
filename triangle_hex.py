from geometer import *

def draw(canvas):
    
    canvas.set_stroke_color(base1)
    canvas.set_fill_color(base03)
    canvas.fill_background()
    
    t = Triangle(3000)
    t.draw(canvas, at_point=canvas.center, rotation=180)
    
    for p in t.points:
        l = Line(center=origin, to_point=p)
        l.draw(canvas, at_point=canvas.center, rotation=180)

    hs = HexagonalRhombus(t.r)
    
    for i in range(3):
        hs.draw(canvas, at_point=canvas.center, rotation=i * 120 + 60)

