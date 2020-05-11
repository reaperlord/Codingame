import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#ver 02, purging numpy

w, h, count_x, count_y = [int(i) for i in input().split()]

def getEmptyList(count):
    sizeOfArray = int ( (count+2) * (count+1)/2)
    r = range(sizeOfArray)
    return ([*r], sizeOfArray-1)

xarray, x_maxIdx = getEmptyList(count_x)
yarray, y_maxIdx = getEmptyList(count_y)

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

def sides(list, count, currentIndex): #give array of all possible sides
    
    for i in range(count): # count indices from first to one before last
        for j in list[i+1:count+1]: #count indices from current to last    
            list[currentIndex] = j - list[i]
            currentIndex += 1
    return sorted(list)

sortedSidesArrayX = sides(xarray, count_x, currentIndexX)
sortedSidesArrayY = sides(yarray, count_y, currentIndexY)

continueLoop = True
x_idx, y_idx = int(0), int(0)
numberOfSquares = 0

while continueLoop:

    if sortedSidesArrayX[x_idx] == sortedSidesArrayY[y_idx]:
        x_multiplier, y_multiplier = 1, 1 #for counting squares of the same number

        #check for x duplicates
        if x_idx != x_maxIdx:

            offsetIdx = 1

            while sortedSidesArrayX[x_idx] == sortedSidesArrayX[x_idx+offsetIdx]: #same x            
                x_multiplier += 1 #add another x_multiplier
                offsetIdx += 1
         
            x_idx += offsetIdx #increment x_index for next loop
        else:
            continueLoop = False #this is the last execution of the loop since there are no more x to compare

        #check for y duplicates
        if y_idx != y_maxIdx:

            offsetIdx = 1

            while sortedSidesArrayY[y_idx] == sortedSidesArrayY[y_idx+offsetIdx]: #same x            
                y_multiplier += 1 #add another x_multiplier
                offsetIdx += 1 #try for next iteration

            y_idx += offsetIdx
        else:
            continueLoop = False #this is the last execution of the loop since there are no more y to compare

        numberOfSquares += x_multiplier * y_multiplier #no of additional squares counted are x multiplier by y multiplier

    elif sortedSidesArrayX[x_idx] > sortedSidesArrayY[y_idx]:
        if y_idx == y_maxIdx: #y is already maximal (the complete height)
            break
        else:
            y_idx += 1 #if the x-val is greater than the y-val, iterate y
            continue
    elif sortedSidesArrayX[x_idx] > sortedSidesArrayY[y_idx]:
        if x_idx == x_maxIdx: #x is maximal therefore break loop
            break
        else:
            x_idx += 1 #if the y-val is greater than the x-val, iterate x
            continue


print(numberOfSquares)
