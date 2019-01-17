from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open('/Users/jiang/Documents/learn/tesseract/test5.png'),lang="chi_sim")
print(text)