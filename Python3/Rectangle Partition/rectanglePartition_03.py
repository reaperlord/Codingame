import sys
import math
import numpy

#trying with scalar product

w, h, count_x, count_y = [int(i) for i in input().split()]

if w > h:
    maxSize = w
else:
    maxSize = h

xVec = numpy.zeros(maxSize, int)
yVec = numpy.zeros(maxSize, int)

xMeasures = numpy.empty(count_x+1, int)
yMeasures = numpy.empty(count_y+1, int)


currentIndexX, currentIndexY = 0, 0


for i in input().split():    
    xMeasures[currentIndexX] = int(i)
    currentIndexX += 1
#at end append width
xMeasures[currentIndexX] = w

for i in input().split():
    yMeasures[currentIndexY] = int(i)
    currentIndexY += 1
#at end append height
yMeasures[currentIndexY] = h

def lengthCounter(vector, measuresArray, count): 
    
    vector[measuresArray[count]-1] += 1 #add one for the max size

    for i in range(count): # count indices from first to one before last
        vector[measuresArray[i]-1] += 1 #add one at that vector dimension for itself
        for j in measuresArray[i+1:count+1]: #count indices from current to last    
            index = int(j - measuresArray[i] -1)
            vector[index] += 1 #add one at that vector dimension (-1 since 0-index = length of 1 (i.e. no reason to waste an index)

        

lengthCounter(xVec, xMeasures, count_x)
lengthCounter(yVec, yMeasures, count_y)


print(numpy.dot(xVec, yVec))
