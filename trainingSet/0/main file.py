from PIL import Image
import numpy
import csv
import os
import test

for l in range(0,41995):
	if os.path.exists('img_'+str(l)+'.jpg'):
		imag = Image.open('img_'+str(l)+'.jpg').convert('L')
		convertImg(imag,l,0)
numpy.savetxt("array.csv",picArray,fmt = "%s")
f = open("array.csv", 'r')
for row in f:
	print(row)
