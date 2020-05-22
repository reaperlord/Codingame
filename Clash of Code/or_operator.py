import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

t = input()
t2 = input()
t3 =""

for i in range(len(t)):
    if t[i] =="1":
        if t2[i]=="0":
            t3+="1"
        else: t3+="0"
    elif t2[i]=="1":
        if t[i]=="0":
            t3+="1"
        else: t3+="0"
    else:
        t3+="0"
        
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print(t3)
