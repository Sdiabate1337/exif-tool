
#!/usr/bin/env python3

# This program is for .JPG and .TIFF format files.
# Installation and usage instructions:
# 1. Install Pillow (Pillow will not work if you have PIL installed):
# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade Pillow
# 2. Add .jpg images  to subfolder ./images from where the script is stored.
# Note most social media sites strip exif data from uploaded photos.

import os
from PIL import Image

cwd = os.getcwd()
os.chdir(os.path.join(cwd, "images"))
files = os.listdir()


if len(files) == 0:
        print("You don't have files in the ./images folder.")
        exit

for file in files:

        try:
           image = Image.open(file)
           img_data = list(image.getdata())
           image_no_exif = Image.new(image.mode , image.size)
           image_no_exif.putdata(img_data)
           image_no_exif.save(file)
        
        except IOError:
            print("file format not supported.")
