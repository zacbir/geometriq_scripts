import random

from geometer import *


class ContextFiller:

    def __init__(self, canvas, fill_color):
        self.canvas = canvas
        self.original_fill_color = canvas.fill_color
        self.fill_color = fill_color

    def __enter__(self):
        self.canvas.set_fill_color(self.fill_color)
        return self.canvas

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.canvas.set_fill_color(self.original_fill_color)


class ContextStroker:

    def __init__(self, canvas, stroke_width, stroke_color):
        self.canvas = canvas
        self.original_stroke_width = canvas.stroke_width
        self.original_stroke_color = canvas.stroke_color
        self.stroke_width = stroke_width
        self.stroke_color = stroke_color

    def __enter__(self):
        self.canvas.set_stroke_width(self.stroke_width)
        self.canvas.set_stroke_color(self.stroke_color)
        return self.canvas

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.canvas.set_stroke_width(self.original_stroke_width)
        self.canvas.set_stroke_color(self.original_stroke_color)


def random_point_within(min_x, max_x, min_y, max_y):
    rand_x = random.random() * (max_x - min_x) + min_x
    rand_y = random.random() * (max_y - min_y) + min_y

    return Point(rand_x, rand_y)


def color_for_point(point, canvas):
    """

    :param point: Point
    :param canvas: CoreGraphicsCanvas
    :return: Color
    """
    line = Line.from_origin_with_slope(Point(canvas.width, 0), 2.0/5.0)
    distance = line.distance_to(point)
    return band(fills, distance, canvas.diagonal, fuzz=True)


def draw(canvas):

    blocks = 5
    inner_margin = 75

    bounds_w = canvas.width / (blocks + 2)
    bounds_h = canvas.height / (blocks + 2)

    for plot_w_idx in range(blocks):
        for plot_h_idx in range(blocks):
            min_x = (plot_w_idx * bounds_w + bounds_w) + 10
            max_x = (plot_w_idx * bounds_w + bounds_w * 2) - 10

            min_y = (plot_h_idx * bounds_h + bounds_h) + 10
            max_y = (plot_h_idx * bounds_h + bounds_h * 2) - 10

            square_center = random_point_within(min_x + inner_margin, max_x - inner_margin, min_y + inner_margin, max_y - inner_margin)

            s = Shape(0)
            southwest = Point(min_x, min_y)
            northwest = Point(min_x, max_y)
            northeast = Point(max_x, max_y)
            southeast = Point(max_x, min_y)

            s.add_point(southwest)
            s.add_point(northwest)
            s.add_point(northeast)
            s.add_point(southeast)

            s.draw(canvas)

            west = ArbitraryTriangle([southwest, northwest, square_center])
            north = ArbitraryTriangle([northwest, northeast, square_center])
            east = ArbitraryTriangle([northeast, southeast, square_center])
            south = ArbitraryTriangle([southeast, southwest, square_center])

            for point in s.points:
                l = Line(square_center, point)
                l.draw(canvas)

            sides = [west, north, east, south]

            color = base00  # color_for_point(Point(min_x, min_y), canvas)

            with ContextStroker(canvas, 0, clear) as fill_only_canvas:
                with ContextFiller(fill_only_canvas, color.alpha(0.5)) as west_canvas:
                    west.draw(west_canvas)
                with ContextFiller(fill_only_canvas, color) as north_canvas:
                    north.draw(north_canvas)
                with ContextFiller(fill_only_canvas, color.alpha(0.75)) as east_canvas:
                    east.draw(east_canvas)
                with ContextFiller(fill_only_canvas, color.alpha(0.25)) as south_canvas:
                    south.draw(south_canvas)
            #
            # fill_one = range(4)                          # Either fill one triangle
            # fill_two = zip(range(4), range(1, 4) + [0])  # Or two, adjacent triangles
            #
            # fill_chance = random.random() * (plot_h_idx + 1)
            #
            # # fill_chance += Point(min_x, min_y).distance_to(origin) / canvas.diagonal
            #
            # if fill_chance < 1:
            #     pair = random.choice(fill_two)
            #     triangles = sides[pair[0]], sides[pair[1]]
            #     with ContextStroker(canvas, 0, clear) as fill_only_canvas:
            #         with ContextFiller(fill_only_canvas, base1) as filled_canvas:
            #             triangles[0].draw(filled_canvas)
            #         with ContextFiller(fill_only_canvas, base00) as filled_canvas:
            #             triangles[1].draw(filled_canvas)
            # elif 1 < fill_chance < 1.75:
            #     triangle = sides[random.choice(fill_one)]
            #     with ContextStroker(canvas, 0, clear) as fill_only_canvas:
            #         with ContextFiller(fill_only_canvas, base1) as filled_canvas:
            #             triangle.draw(filled_canvas)
