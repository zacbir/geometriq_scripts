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
    
    definitions = set()
    
    for i in range(num_circles):
        
        radius = fib.next()
        
        segments = 6
        
        for s in range(segments):
            circle = (
                radius,
                Point(origin.x + radius,  origin.y),
                band(fills, i, num_circles),
                s * (360 / segments)
            )
            
            definitions.add(circle)

    for circle_def in definitions:
        radius, center, fill, rotation = circle_def
        c = Circle(radius, center=center)
        canvas.set_fill_color(fill.hair())
        c.draw(canvas, at_point=canvas.center, rotation=rotation)
