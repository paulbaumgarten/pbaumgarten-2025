"""Utility to convert images to raw RGB565 format.

Usage:
    python img2rgb565.py <your_image>
    <your_image> is the full path to the image file you want to convert.
"""

from PIL import Image
from struct import pack
from os import path
import os
import sys

def error(msg):
    print (msg)
    sys.exit(-1)

def write_bin(f, pixel_list):
    for pix in pixel_list:
        r = (pix[0] >> 3) & 0x1F
        g = (pix[1] >> 2) & 0x3F
        b = (pix[2] >> 3) & 0x1F
        f.write(pack('>H', (r << 11) + (g << 5) + b))

def convert_file(in_file, out_file):
    img = Image.open(in_file).convert('RGB')
    pixels = list(img.getdata())
    with open(out_file, 'wb') as f:
        write_bin(f, pixels)
    print('Saved: ' + out_file)

if __name__ == '__main__':
    files = os.listdir("..")
    for file in files:
        if file.endswith(".png"):
            in_file = "..\\" + file
            out_file = in_file.replace(".png",".raw")
            convert_file(in_file, out_file)
