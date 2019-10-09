#!/usr/bin/env python

import argparse
from datetime import datetime
import os
import os.path

try:
    import console
except ImportError:
    console = None

from geometer import *

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Geometer up some art.')
    parser.add_argument('-g', dest='geometer_script', help='a script name')
    parser.add_argument('-x', dest='width', type=int, help='width of the canvas')
    parser.add_argument('-y', dest='height', type=int, help='height of the canvas')
    parser.add_argument('-o', dest='output_dir', help='directory in which to save resulting image')
    parser.add_argument('-c', dest='contrast', help='contrast theme: "light" or "dark"', default='light')

    args = parser.parse_args()

    DEBUG = os.getenv("GEOMETER_DEBUG", False)

    script_name = os.path.splitext(args.geometer_script)[0]
    dated_name = "{}_{}x{}_{}".format(script_name, args.width, args.height, datetime.now().strftime('%Y-%m-%d-%H:%M:%S'))

    script = __import__('geometer_scripts.{}'.format(script_name), globals(), locals(), ['draw'], 0)

    outputDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), args.output_dir)
    filename = os.path.join(outputDir, "{}".format(dated_name))

    canvas = CoreGraphicsCanvas(filename, args.width, args.height, debug=DEBUG)
    canvas.set_miter_limit(15)
    canvas.set_line_cap(kCGLineCapRound)
    canvas.set_line_join(kCGLineJoinMiter)
    canvas.set_stroke_color(clear)
    canvas.set_stroke_width(4)
    canvas.set_fill_color(base3 if args.contrast == "light" else base03)
    
    canvas.fill_background()
    
    canvas.set_stroke_color(base01 if args.contrast == "light" else base1)
    canvas.set_fill_color(clear)
    
    try:
        script.draw(canvas)
    except KeyboardInterrupt:
        pass
    finally:
        output = canvas.save()
    
    if output and console:
        console.show_image(output)
