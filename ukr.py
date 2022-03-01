#!/usr/bin/env python

import os
import sys
from PIL import Image, ImageDraw as D

current_file = os.path.join(sys.argv[1])

current_image = Image.open(current_file, 'r').convert("RGBA")

newName = "ukr_" + current_file

current_file = os.path.join(newName)

box = Image.new("RGBA", current_image.size, (255, 255, 255, 0))
draw = D.Draw(box)
draw.rectangle([(0, 0), (current_image.width, .5 * current_image.height)], fill=(0, 87, 184, 190))  # 190 for ~75% opacity
draw.rectangle([(0, .5 * current_image.height), (current_image.size)], fill=(254, 221, 0, 190))  # 190 for ~75% opacity

out = Image.alpha_composite(current_image, box)

current_image.save(current_file)

out.show()