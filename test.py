from PIL import Image

imag = Image.open('0.jpg').convert('L')  # convert image to 8-bit grayscale
	

def convertImg(img):
	WIDTH, HEIGHT = img.size
	picArray = 

	data = list(img.getdata()) # convert image data to a list of integers
	# convert that to 2D list (list of lists of integers)
	data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]

	# At this point the image's pixels are all in memory and can be accessed
	# individually using data[row][col].

	# For example:
	for x in range(0,27):
		for y in range(0,27): 
			print data[x][y]

	# Here's another more compact representation.

convertImg(imag)