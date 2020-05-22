import sys
import math
#this is a message
#Tiam his s  essage
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a,m= input().split(" ",1)

m = a[0]+m
indx, a_indx=1, 1
while(True):
    if indx == len(m):break
    elif m[indx]==" ": 
        m= m[:indx+1] + a[a_indx] +m[indx+1:]        
        a_indx += 1
        indx+= 2
    else: indx += 1



print(m)
