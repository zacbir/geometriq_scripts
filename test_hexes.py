from geometer import *


def draw(canvas):
    hexagon = HorizontalHexagon(1024, canvas.center)
    arc = Arc(hexagon.size / 2, 120)
    
    hexagon.draw(canvas)

    canvas.set_stroke_color(red)

    arc.draw(canvas, at_point=hexagon.points[1], rotation=120)

    arc.draw(canvas, at_point=hexagon.points[3], rotation=0)

    arc.draw(canvas, at_point=hexagon.points[5], rotation=-120)

    canvas.set_stroke_color(green)

    arc.draw(canvas, at_point=hexagon.points[0], rotation=180)

    arc.draw(canvas, at_point=hexagon.points[2], rotation=60)

    arc.draw(canvas, at_point=hexagon.points[4], rotation=-60)


