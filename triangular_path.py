from math import radians, tan
import random
from geometer import *


def n_dot_down(triangle):
    return (
        (Arc(triangle.AB.length / 2, 60), triangle.points[1], -120),
        (Line(Line(triangle.center, triangle.CA.midpoint).midpoint, triangle.CA.midpoint), None, None)
    )


def n_dot_left(triangle):
    return (
        (Arc(triangle.AB.length / 2, 60), triangle.points[2], 120),
        (Line(Line(triangle.center, triangle.AB.midpoint).midpoint, triangle.AB.midpoint), None, None)
    )


def n_dot_right(triangle):
    return (
        (Arc(triangle.AB.length / 2, 60), triangle.points[0], 0),
        (Line(Line(triangle.center, triangle.BC.midpoint).midpoint, triangle.BC.midpoint), None, None)
    )


def s_dot_up(triangle):
    return (
        (Arc(triangle.AB.length / 2, 60), triangle.points[2], 60),
        (Line(Line(triangle.center, triangle.AB.midpoint).midpoint, triangle.AB.midpoint), None, None)
    )


def s_dot_left(triangle):
    return (
        (Arc(triangle.AB.length / 2, 60), triangle.points[1], -180),
        (Line(Line(triangle.center, triangle.CA.midpoint).midpoint, triangle.CA.midpoint), None, None)
    )


def s_dot_right(triangle):
    return (
        (Arc(triangle.AB.length / 2, 60), triangle.points[0], -60),
        (Line(Line(triangle.center, triangle.BC.midpoint).midpoint, triangle.BC.midpoint), None, None)
    )


n_funcs = (n_dot_down, n_dot_left, n_dot_right)
s_funcs = (s_dot_up, s_dot_left, s_dot_right)


def draw(canvas):

    canvas.debug = False
    size = 256
    
    up_grid = HorizontalHexagonGrid(canvas.center, size, 20, 5)
    vertex_grid = HorizontalHexagonGrid(Point(canvas.center.x, canvas.center.y + (up_grid.step - up_grid.r)), size, 24, 24)
    down_grid = HorizontalHexagonGrid(Point(canvas.center.x + up_grid.size, canvas.center.y + (up_grid.step + up_grid.r)), size, 22, 6)

    canvas.set_stroke_color(base2)

    def draw_choice(function, triangle):
        operations = function(triangle)
        for shape, at, rotation in operations:
            if at:
                shape.draw(canvas, at_point=at, rotation=rotation)
            else:
                shape.draw(canvas)

    for p in up_grid.points:
        t = NorthTriangle(size, p, vertex_grid)
        canvas.set_stroke_width(1)
        t.draw(canvas)
        f = random.choice(n_funcs)
        canvas.set_stroke_width(32)
        draw_choice(f, t)
    
    for p in down_grid.points:
        t = SouthTriangle(size, p, vertex_grid)
        canvas.set_stroke_width(1)
        t.draw(canvas)
        f = random.choice(s_funcs)
        canvas.set_stroke_width(32)
        draw_choice(f, t)
