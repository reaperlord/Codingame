import sys
import math
import collections as col

seqStr = input() #current sequence val as string
end_n = int(input())
current_n = 1

dic = {seqStr : 0} #start of dictionary

while current_n != end_n:

    if seqStr in dic:
        next_seqStr = str(dic[seqStr])    
    else: #seqStr new        
        next_seqStr = str(0)
        dic[seqStr] = 0

    for key, val in dic.items():
        if key == seqStr:
            dic[key] = 1 #reset counter for seqStr
        else:
            dic[key] += 1 #count up

    seqStr = next_seqStr
    current_n += 1

print(seqStr)
