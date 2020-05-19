import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input().split()
output= ''.join(chr(int(i)) for i in message)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

a=output.split()
newArray=[]
for word in a:
	newWord=word[::-1]
	newArray.append(newWord)

output=' '.join(newArray)


print(output)
