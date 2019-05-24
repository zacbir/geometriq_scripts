from geometer import *


def draw(canvas):

    # From a given equilateral triangle, calculate three more triangles:

    triangles_to_draw = set()

    starter = NorthTriangle(2048, canvas.center)
     