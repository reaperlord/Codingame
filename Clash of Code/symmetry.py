import sys
import math
import numpy

def xsymmetry(A):
    if A=="(":
        return ")"
    elif A==")":
        return "("
    elif A=="/":
        return "\\"
    elif A=="\\":
        return "/"
    elif A=="|":
        return "|"
    elif A=="-":
        return "-"

def ysymmetry(A):
    if A=="\\":
        return "/"
    elif A=="/":
        return "\\"
    else: return A
    
isXSymmetric = True
isYSymmetric = True
n = int(input())

array = numpy.empty([n,n])

for i in range(n):
    array[i] = input()


#test for x-symmetry


print("answer")
