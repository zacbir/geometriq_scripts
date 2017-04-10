#!/usr/bin/env python

import argparse
import os
import sys

from geometer import *

if __name__ == '__main__':
    script_name = os.path.splitext(sys.argv[1])[0]
    script = __import__(script_name, globals(), locals(), ['draw'], -1)

    outputDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'output')
    filename = os.path.join(outputDir, "{}".format(script_name))

    canvas = CoreGraphicsCanvas(filename, )
    script.draw(canvas)

    canvas.save()
