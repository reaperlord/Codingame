
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

ccurrentMaxchar=""
currentMaxCount=0

currentChar=""
currentCharCounter=0
for char in s:
    if currentChar==char:
        currentCharCounter+=1
    else:
        if currentCharCounter > currentMaxCount:
                currentMaxCount = currentCharCounter
                currentMaxchar= currentChar
        
        currentCharCounter=1
        currentChar=char

if currentCharCounter > currentMaxCount:
                currentMaxCount = currentCharCounter
                currentMaxchar= currentChar


print(currentMaxchar+" " +str(currentMaxCount))