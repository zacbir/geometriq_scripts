import random
from geometer import *


def draw(canvas):
    """
    Make some pretty and draw it to `canvas`.

    :param canvas: CoreGraphicsCanvas
    :return: None
    """
    canvas.set_stroke_color(clear)
    reference_path = os.getenv("REFERENCE_IMAGE_PATH")

    reference = None
    if reference_path:
        reference = ReferenceImage(reference_path, canvas)

    grid = SquareGrid(canvas.center, 32, 64, 64)

    for p in grid.points:
        reference_point = reference.transform_point(p)
        reference_color = reference.color_at_point(reference_point)
        reference_grey_idx = reference_color.greyscale().r  # point between 0.0-1.0, maps white-black
        size = band(range(24), int((1.0 - reference_grey_idx) * 255), 255)

        canvas.set_fill_color(reference_color)
        c = Circle(size, p)
        c.draw(canvas)
