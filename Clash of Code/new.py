import sys
import math
#this is a message
#Tiam his s  essage
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a,m= input().split(" ",1)

m = a[0]+m
indx, a_indx=1, 
while(True):
    if indx == len(m):break
    elif m[indx]==" ": 
        m= m[:indx+1] + a[a_indx] +m[indx+1:]
        (indx, a_indx) += (2, 1)


for i in range(len(a[0])):
    n+=a[i]+m[i]+" "

print(n[:-1])
