from math import sqrt
from geometer import *

def F():
    a,b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b
    
def draw(canvas):
    num_circles = 19
    fib = F()
    
    lines = [Line(center=origin, to_point=canvas.center), Line(center=Point(0, canvas.height), to_point=canvas.center), Line(center=Point(canvas.width, canvas.height), to_point=canvas.center), Line(center=Point(canvas.width, 0), to_point=canvas.center)]
    
    for i in range(num_circles):
        
        radius = fib.next()
        
        for line in lines:
            p = line.point_from_center(sqrt(radius**2 + radius**2))
            c = Circle(radius, center=p)
            fill = band(fills, i, num_circles)
            canvas.set_fill_color(fill.hair())
            c.draw(canvas, at_point=origin)
