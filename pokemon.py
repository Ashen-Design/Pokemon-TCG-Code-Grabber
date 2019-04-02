import sys
import clipboard
import PIL
from PIL import ImageGrab
from PIL import Image
import cv2
import pytesseract

img = ImageGrab.grabclipboard()
new_size = tuple(4*x for x in img.size)
img = img.resize(new_size, Image.ANTIALIAS)
img.save('pkmn.png', 'PNG')

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"


if img is None:
    print("Nothing copied")
else:
    print("Image grabbed")
    cvimg = cv2.imread("pkmn.png", 0)
    cv2.imshow('image',cvimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    text = pytesseract.image_to_string(Image.open('pkmn.png'), config="-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz- -psm 6")
    print(text)
    clipboard.copy(text)
sys.exit()