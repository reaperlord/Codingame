b=o=""
for c in input():b+=format(ord(c),"07b")
b+="2"
l,n=b[0],1
for i in range(1,len(b)):
 if b[i]==l:n+=1
 else:
  o+=" %s %s"%("0"if l=="1"else"00",n*"0")
  l,n=b[i],1
print(o[1:])