import sys
import math
import numpy

#first try

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

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
    return currentIndex

currentIndexX = sides(xarray, count_x, currentIndexX)
currentIndexY = sides(yarray, count_y, currentIndexY)

def uniqueList (array: numpy.ndarray):
        
    uniqueList = [] # a list of values
    multiplierList = [] #a list of value
    blacklistIndx = [] #indices not to check

    for index in range(array.size):
        if index in blacklistIndx:
            continue
        else:
            uniqueList.append(array[index])
            multiplier = 1
            for index2 in range(index+1,array.size):
                if array[index] == array[index2]:
                    multiplier += 1
                    blacklistIndx.append(index2)
            multiplierList.append(multiplier)

    return (uniqueList, multiplierList)

x_unique = uniqueList(xarray)
y_unique = uniqueList(yarray)
  
numberOfSquares = 0

for x_idx in range(len(x_unique[0])):
    for y_idx in range(len(y_unique[0])):
        if x_unique[0][x_idx] == y_unique[0][y_idx]:
            numberOfSquares += x_unique[1][x_idx] * y_unique[1][y_idx]





# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print(numberOfSquares)
