from geometer import *

def F():
    a,b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b
    
def draw(canvas):
    num_circles = 32
    fib = F()
    
    for i in range(num_circles):
        
        radius = fib.next()
        c = Circle(radius, center=Point(origin.x + radius, origin.y))
        fill = band(fills, i, num_circles)
        canvas.set_fill_color(fill.hair())
        c.draw(canvas, at_point=canvas.center, rotation=i * (360 / num_circles))
