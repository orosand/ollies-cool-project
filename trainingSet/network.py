# Read in array
# assign values to results based on weights


import numpy as np
import os
import random
import csv
#make the weights array
weights = np.zeros([784,10], dtype = int)
for x in range(784):
	for y in range(10):
		weights[x][y] = random.randint(0,10)
pixels = [] 
results = [0,0,0,0,0,0,0,0,0,0]

#open the array and convert it into the pixel array
data = np.genfromtxt('array1.csv', delimiter=",")

		
print data[1]
	
for v in range(0,10):
	for n in range(0,784): 

def perturb(weightX,weightY, chance, min, max):
	percent = random.randint(0,100)
	if (percent<=chance):
		weights[weightX][weightY] = weights[weightX][weightY] + random.randint(min,max)

perturb(12,2,18,-1,1)
# print weights[12][2]




