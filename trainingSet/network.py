# array 784x10
# array for each pixel
# array 10x1
# assign random values to each
# save weights to a csv
# perturb weight, randomize within a min and max with a prob and an amount it can be changed


import numpy
import os
import random
import csv
#make the weights array
weights = numpy.zeros([784,10], dtype = int)
for x in range(784):
	for y in range(10):
		weights[x][y] = random.randint(0,10)
pixels = [] 

#open the array and convert it into the pixel array
def openConvert(filename):
	# with open('array.csv') as csvfile:
	# 	reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
	# 	print(reader)
		# for row in reader:
			
		# 	data = numpy.asarray(row)
		# 	pixels = data
		# 	break

	data = list(csv.reader(open('array.csv')))
	print(data[1])


def perturb(weightX,weightY, chance, min, max):
	percent = random.randint(0,100)
	if (percent<=chance):
		weights[weightX][weightY] = weights[weightX][weightY] + random.randint(min,max)

perturb(12,2,18,-1,1)
# print weights[12][2]

openConvert('')


