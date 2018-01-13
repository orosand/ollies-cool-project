from PIL import Image
import numpy
imag = Image.open('0.jpg').convert('L')  # convert image to 8-bit grayscale
imag2 = Image.open('img_1.jpg').convert('L')  # convert image to 8-bit grayscale
	
picArray = numpy.empty([2,100], dtype = object)
def convertImg(img,numb,result):
	WIDTH, HEIGHT = img.size
	value = [] 

	data = list(img.getdata()) # convert image data to a list of integers
	# convert that to 2D list (list of lists of integers)
	data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]

	# At this point the image's pixels are all in memory and can be accessed
	# individually using data[row][col].
	for x in range(0,27):
		for y in range(0,27): 
			value.append(data[x][y])
	picArray[numb][0] = value
	picArray[numb][1] = result
	print picArray
	# Here's another more compact representation.

convertImg(imag,0,0)
convertImg(imag2,1,2)


