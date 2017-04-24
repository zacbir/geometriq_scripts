from geometer import *

def draw(canvas):
    canvas.set_fill_color(clear)
    canvas.set_stroke_width(16)
    
    for i, color in enumerate((yellow, orange, red)):
        canvas.set_stroke_color(color)
        c = Circle((i + 1) * 500)
        c.draw(canvas, at_point=canvas.center)
    
    t_ref = Triangle(1500)
    t = Triangle(t_ref.size, center=Point(origin.x, origin.y - (t_ref.step - t_ref.r)))
    for i in range(3):
        t.draw(canvas, at_point=canvas.center, rotation=i * 120)

