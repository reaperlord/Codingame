import sys
import math
import numpy

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n, x= [int(i) for i in input().split()]
l=numpy.zeros(x)
for i in range(n):
    a, b = [int(j) for j in input().split()]
    for c in range(a,b):
        l[c]+=1

mini = int(numpy.amin(l))

print(mini)
print(int(numpy.amax(l)))
