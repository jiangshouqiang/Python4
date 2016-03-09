from PIL import Image ,ImageFilter

im = Image.open("test.jpg")
img = im.filter(ImageFilter.BLUR)
img.save('blur.jpg','jpeg')