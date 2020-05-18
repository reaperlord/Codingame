import sys
import math

w=['Dr','Mr','Mrs','Ms','Lord','Lady','Sir','BA','LLB','MD','PhD','Jr','Snr','Jnr,','Snr,']
n = int(input())
for i in range(n):
    name = input().split(" ")
    t=""
    for part in name:        
        if part in w: continue
        else: t += part[0]+"."
    print(t)
