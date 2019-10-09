from geometer import *


def draw(canvas):

    paths = [
        Line(Point(4, 12), Point(4, 4)),
        Line(Point(12, 12), Point(4, 12)),
        Line(Point(12, 4), Point(12, 12)),
        Line(Point(4, 4), Point(12, 4))
    ]

    canvas.set_stroke_width(1)
    CGContextBeginPath(canvas.context)
    for path in paths:
        
        CGContextAddPath(canvas.context, )
    CGContextClosePath(canvas.context)
    CGContextMoveToPoint(canvas.context, 15, 15)
    CGContextAddLineToPoint(canvas.context, 15, 15)
    CGContextDrawPath(canvas.context, kCGPathFillStroke)
