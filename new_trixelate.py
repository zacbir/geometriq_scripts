import random
from geometer import *


def draw(canvas):
    """
    Make some pretty and draw it to `canvas`.

    :param canvas: CoreGraphicsCanvas
    :return: None
    """
    reference_path = os.getenv("REFERENCE_IMAGE_PATH")

    reference = None
    if reference_path:
        reference = ReferenceImage(reference_path, canvas)

    right_grid = HorizontalHexagonGrid(canvas.center, 60, 50, 50)
    vertex_grid = HorizontalHexagonGrid(Point(canvas.center.x + (right_grid.step - right_grid.r), canvas.center.y), 60,
                                      60, 60)
    left_grid = HorizontalHexagonGrid(Point(canvas.center.x + (right_grid.size / 2.0), canvas.center.y + right_grid.r),
                                    60, 50, 50)

    canvas.set_stroke_width(0.5)

    for point in right_grid.points:
        reference_point = reference.transform_point(point)
        reference_color = reference.color_at_point(reference_point)

        canvas.set_stroke_color(canvas.stroke_color.shade())
        canvas.set_fill_color(reference_color.midtone())

        t = NorthTriangle(right_grid.size, center=point, grid=vertex_grid)
        t.draw(canvas)

    for point in left_grid.points:
        reference_point = reference.transform_point(point)
        reference_color = reference.color_at_point(reference_point)

        canvas.set_stroke_color(canvas.stroke_color.shade())
        canvas.set_fill_color(reference_color.midtone())

        t = SouthTriangle(left_grid.size, center=point, grid=vertex_grid)
        t.draw(canvas)
