import sys
import math
import numpy

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#optimization

w, h, count_x, count_y = [int(i) for i in input().split()]

def getEmptyArray(count):
    sizeOfArray = int ( (count+2) * (count+1)/2)
    return numpy.empty(sizeOfArray, int)

xarray, yarray = getEmptyArray(count_x), getEmptyArray(count_y)

currentIndexX, currentIndexY = 0, 0


for i in input().split():    
    xarray[currentIndexX] = int(i)
    currentIndexX += 1
#at end append width
xarray[currentIndexX] = w
currentIndexX += 1

for i in input().split():
    yarray[currentIndexY] = int(i)
    currentIndexY += 1
#at end append height
yarray[currentIndexY] = h
currentIndexY += 1

def sides(array, count, currentIndex): #give array of all possible sides
    
    for i in range(count): # count indices from first to one before last
        for j in array[i+1:count+1]: #count indices from current to last    
            array[currentIndex] = j - array[i]
            currentIndex += 1
    return numpy.unique(array, return_counts = True)

sortedSidesArrayX = sides(xarray, count_x, currentIndexX)
sortedSidesArrayY = sides(yarray, count_y, currentIndexY)

continueLoop = True
x_idx, y_idx = int(0), int(0)
numberOfSquares = 0

while continueLoop:

    if sortedSidesArrayX[0][x_idx] == sortedSidesArrayY[0][y_idx]:
        numberOfSquares += sortedSidesArrayX[1][x_idx] * sortedSidesArrayY[1][y_idx]
        if sortedSidesArrayX[0][x_idx] != w: #if x is not already at max
            x_idx += 1
        else: break #x was at max => makes no sense to continue 
    elif sortedSidesArrayX[0][x_idx] > sortedSidesArrayY[0][y_idx]:
        if sortedSidesArrayY[0][y_idx] == h: #y is already maximal (the complete height)
            break
        else:
            y_idx += 1 #if the x-val is greater than the y-val, iterate y
            continue
    elif sortedSidesArrayX[0][x_idx] > sortedSidesArrayY[0][y_idx]:
        if sortedSidesArrayX[0][x_idx] == w: #x is maximal therefore break loop
            break
        else:
            x_idx += 1 #if the y-val is greater than the x-val, iterate x
            continue


print(numberOfSquares)
