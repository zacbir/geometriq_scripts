from geometer import *


def draw(canvas):
    points = [
        Point(1300, 1300),
        Point(1600, 1700),
        Point(1800, 1200)
    ]

    control_points = [
        Point(1500, 1600),
        Point(1800, 1600),
        Point(1400, 1100)
    ]

    curves = (
        Curve([points[0], points[1]], [control_points[0]]),
        Curve([points[1], points[2]], [control_points[1]]),
        Curve([points[2], points[0]], [control_points[2]])
    )

    starting_point = points.pop(0)
    CGContextMoveToPoint(canvas.context, starting_point.x, starting_point.y)
    for next_point in points:
        cp = control_points.pop(0)
        CGContextAddQuadCurveToPoint(canvas.context, cp.x, cp.y, next_point.x, next_point.y)
    cp = control_points.pop()
    CGContextAddQuadCurveToPoint(canvas.context, cp.x, cp.y, starting_point.x, starting_point.y)
    CGContextClosePath(canvas.context)
    CGContextDrawPath(canvas.context, kCGPathFillStroke)