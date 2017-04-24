import random

from geometer import *

def draw(canvas):
    for i in range(4):
        canvas.set_fill_color(random.choice(solarized).shade())
        from_x = i * canvas.width / 4
        to_x = (i + 1) * canvas.width / 4
        r = Rectangle(Point(to_x, canvas.height), center=Point(from_x, 0))
        r.draw(canvas, at_point=origin)
    
    for j in range(10):
        p = Point(random.random() * canvas.width, random.random() * canvas.height)
        for k in range(int(round(random.random() * 6))):
            width = random.random() * 20
            canvas.set_stroke_width(width)
            canvas.set_stroke_color(random.choice(solarized).shade())
            canvas.set_fill_color(random.choice(solarized).shade())
            c = Circle(random.random() * 512)
            c.draw(canvas, at_point=p)

