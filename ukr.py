#!/usr/bin/env python

import os
import sys
from pathlib import Path
from PIL import Image, ImageDraw as D

current_file = os.path.join(sys.argv[1])

if current_file.endswith(".jpg"):
    basename = Path(current_file).stem
    convert_image = Image.open(current_file)
    convert_image = convert_image.save(basename + ".png", format="png")
    converted_name = basename + ".png"
    current_file = converted_name
    current_image = Image.open(current_file)
    print('success')
else:
    current_image = Image.open(current_file)

newName = "ukr_" + current_file

current_file = os.path.join(newName)

box = Image.new("RGBA", current_image.size, (255, 255, 255, 0))
draw = D.Draw(box)
draw.rectangle([(0, 0), (current_image.width, .5 * current_image.height)], fill=(0, 87, 184, 190))  # 190 for ~75% opacity
draw.rectangle([(0, .5 * current_image.height), (current_image.size)], fill=(254, 221, 0, 190))  # 190 for ~75% opacity


to_rgba = current_image.convert("RGBA")

out = Image.alpha_composite(to_rgba, box)

out.save(current_file)

out.show()  # optional
