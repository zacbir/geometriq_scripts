from geometer import *


def draw(canvas):

    points = (
        (Point(canvas.width / 3.0, (canvas.height * 2.0) / 3.0), red),
        (Point((canvas.width * 2.0) / 3.0, canvas.height / 2.0), green),
        (Point(canvas.width / 3.0, canvas.height / 3.0), blue)
    )

