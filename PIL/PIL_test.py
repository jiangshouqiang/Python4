from PIL import Image

im = Image.open('test.jpg')
#get width , height of the image
w , h = im.size
print("Original image size : %sx %s " % (w,h))
im.thumbnail((w//2,h//2))
print('Resize image to : %sx %s' % (w//2,h//2))

im.save('test_result.jpg','jpeg')

