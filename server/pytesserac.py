import pytesseract
from PIL import Image

img_file = "./assets/bowers.jpg"
no_noise = "./temp/no_noise.jpg"

img = Image.open(no_noise)

ocr_result = pytesseract.image_to_string(img)

print(ocr_result)
