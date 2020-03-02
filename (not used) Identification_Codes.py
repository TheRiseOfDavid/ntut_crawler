# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 18:32:42 2020

@author: user
"""

from PIL import Image
from pyocr import tesseract
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\program\tool program\Download_NTUT_Imfornation_Learning_Course_Files\element\Tesseract-OCR\tesseract.exe'
image = Image.open('./element/FYAG.png')
save_Image = image.convert('RGB')
save_Image.save('./element/FYAG.jpg')

image = Image.open('./element/FYAG.jpg')
print(image)
code= pytesseract.image_to_string(image)
print(code)
