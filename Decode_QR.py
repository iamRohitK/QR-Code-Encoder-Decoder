# pyzbar is a pure Python library that reads one-dimensional barcodes and QR codes using the zbar library
from pyzbar.pyzbar import decode

# Ref: https://www.geeksforgeeks.org/python-pillow-a-fork-of-pil/
# Python Imaging Library (expansion of PIL) is the de facto image processing package for Python language. 
# This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.

from PIL import Image

img = Image.open('C:/Programming/Projects/QR-Code-Encoder-Decoder/myqrcode2.png')

result = decode(img)
print(result)