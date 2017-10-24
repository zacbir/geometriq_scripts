from geometer import *


def draw(canvas):
    point_1 = origin
    point_2 = Point(canvas.width, canvas.height)

    steps = 32

    steps_x = canvas.width / float(steps)
    steps_y = canvas.height / float(steps)

    for i in range(steps):
        control_point = Point(i * steps_x, canvas.height - (i * steps_y))
        c = Curve([point_1, point_2], [control_point, control_point])
        canvas.set_stroke_color(band(fills, control_point.distance_to(canvas.center), canvas.diagonal / 2.0))
        c.draw(canvas)

    point_3 = Point(0, canvas.height)
    point_4 = Point(canvas.width, 0)

    for j in range(steps):
        control_point = Point(j * steps_x, j * steps_y)
        c = Curve([point_3, point_4], [control_point, control_point])
        canvas.set_stroke_color(band(fills, control_point.distance_to(canvas.center), canvas.diagonal / 2.0))
        c.draw(canvas)
