from PIL import Image
import numpy
import csv
import os
	
picArray = numpy.zeros([41999,1], dtype = object)
def convertImg(img,numb,result):
	WIDTH, HEIGHT = img.size
	value = [] 

	data = list(img.getdata())
	data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]


	for x in range(0,27):
		for y in range(0,27): 
			value.append(data[x][y])
	picArray[numb][0] = value
	# picArray[numb][0] = result

	


for n in range(0,10):
	os.chdir("/Users/benrosand/Documents/GitHub/ollies-cool-project/trainingSet")
	os.chdir(os.getcwd()+"/"+str(n))
	print os.getcwd()

	for l in range(0,41999):
		if os.path.exists('img_'+str(l)+'.jpg'):
			imag = Image.open('img_'+str(l)+'.jpg').convert('L')
			convertImg(imag,l,n)


os.chdir("/Users/benrosand/Documents/GitHub/ollies-cool-project/trainingSet")

numpy.savetxt("array.csv",picArray,fmt = "%s")