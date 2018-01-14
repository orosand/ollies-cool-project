from PIL import Image
import numpy
import csv
import os
imag = Image.open('img_4.jpg').convert('L')  # convert image to 8-bit grayscale
imag2 = Image.open('img_1.jpg').convert('L')  # convert image to 8-bit grayscale
	
picArray = numpy.zeros([2,2], dtype = object)
def convertImg(img,numb,result):
	WIDTH, HEIGHT = img.size
	value = [] 

	data = list(img.getdata()) # convert image data to a list of integers
	data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]


	for x in range(0,27):
		for y in range(0,27): 
			value.append(data[x][y])
	picArray[numb][0] = value
	picArray[numb][1] = result

	print picArray[0][0][0]

convertImg(imag,0,0)
convertImg(imag2,1,2)
numpy.savetxt("array.cv",picArray,fmt = "%s")
f = open("array.cv", 'r')
for row in f:
	print(row)
cd /1
