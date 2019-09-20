
import pytesseract
from PIL import Image

image = Image.open('./images/tesseracttest.jpg')
#image = Image.open('./images/recaptcha.png')

text = pytesseract.image_to_string(image)
print(text)


