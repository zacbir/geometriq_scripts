from geometer import *

def draw(canvas):

    pairs = (
        (magenta, violet),
        (blue, violet),
        (blue, cyan),
        (green, cyan),
        (green, yellow),
        (orange, yellow),
        (orange, red),
        (magenta, red),
    )
    
    s = Square(128)

    for p_idx, pair in enumerate(pairs):
        start, end = pair
        
        for i, new_color in enumerate(start.gradient_to(end, 32)):

            center = Point(64 + (128 * i), 64 + (128 * p_idx))

            canvas.set_fill_color(new_color)

            s.draw(canvas, at_point=center)
