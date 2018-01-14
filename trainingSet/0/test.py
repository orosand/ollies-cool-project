from PIL import Image
import numpy
import csv
import os
	
picArray = numpy.zeros([41995,2], dtype = object)
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

	



for l in range(0,41995):
	if os.path.exists('img_'+str(l)+'.jpg'):
		imag = Image.open('img_'+str(l)+'.jpg').convert('L')
		convertImg(imag,l,0)
numpy.savetxt("array.csv",picArray,fmt = "%s")
f = open("array.csv", 'r')
for row in f:
	print(row)

