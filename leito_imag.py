import pytesseract
import cv2
import re
import time as tm


caminho = r"C:\\Users\\aprendiz.ti\\AppData\\Local\\Programs\\Tesseract-OCR"

img = cv2.imread('4.png')


pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
texto = pytesseract.image_to_string(img, lang= "por")


print(texto)