from geometer import *

def draw(canvas):
    full_size = 1024
    
    for i in range(360):
        
        scale = (i * (1 + 1/12.0)) / 360.0
        
        p = Point(scale * full_size, 0)
        
        c = Circle(scale * full_size, p)
        stroke = band(fills, i, 360)
        canvas.set_stroke_color(stroke.half())
        c.draw(canvas, at_point=Point(canvas.center.x - 512, canvas.center.y), rotation=i * (1 + 1/12.0))

