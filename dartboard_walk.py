from math import sqrt, ceil

from geometer import *

def draw(canvas):

    strokes = [base1, clear]

    center = Point(random.random() * canvas.width, random.random() * canvas.height)
    angles = sorted(random.sample(range(360), 72))
    radius_step = 50
    canvas.set_stroke_width(50)
    canvas.set_line_cap(kCGLineCapButt)

    max_diagonal = sqrt((canvas.width / 2)**2 + (canvas.height / 2)**2)

    for i in range(int(ceil(canvas.longest_distance_from(center) / radius_step))):

        start_idx = i % 2
        radius = i * radius_step

        start_angle = 0

        for j in range(len(angles)):
            try:
                end_angle = angles[j + 1]
            except IndexError:
                end_angle = 360
            arc_angle = end_angle - start_angle

            a = Arc(radius, arc_angle)

            stroke = strokes[j % 2 - start_idx]
            canvas.set_stroke_color(stroke)
            a.draw(canvas, at_point=center, rotation=start_angle)

            start_angle = end_angle
            
