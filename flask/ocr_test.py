import os
from PIL import Image
from pytesseract import *
import re
import cv2

tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'

dir = os.path.dirname(os.path.abspath(__file__))
dir = dir+'./input_frame/'
filename = input("filename: ")
arr = filename.split('.')
output = "./output/"+arr[0]+".txt"

image = cv2.imread(dir+filename)

# Image preprocessing: gray scale, threshold
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
text = image_to_string(gray, lang='eng+kor', config=tessdata_dir_config)

cv2.imshow('original', image)
cv2.imshow('gray', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

with open(output, "w", -1, "utf-8") as f:
    f.write(text)
