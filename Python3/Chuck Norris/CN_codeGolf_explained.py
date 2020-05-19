b=o=""#initialization of (b)inaryString and (o)utput string
for c in input():b+=format(ord(c),"07b") #for each char in inputString, get ascii coder, then format to 7-bit length and append to binary string
b+="2" #add a dummy value to binary string (saves us a conversion line => see non code golf version)
l,n=b[0],1 # initialize (l)astChar = first char of binary string, (n)umber of times char has been in the current series = is 1 of course
for i in range(1,len(b)): 
 if b[i]==l:n+=1 #if current index is equal to last index increase counter by 1
 else:
  o+=" %s %s"%("0"if l=="1"else"00",n*"0") #format string according to requirements
  l,n=b[i],1 #reset lastChar to current char, and counter to 1
print(o[1:]) #print (o)utput string omitting first space