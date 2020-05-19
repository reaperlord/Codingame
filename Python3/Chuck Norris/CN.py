#solution for
#https://www.codingame.com/ide/puzzle/chuck-norris-codesize

binary=output=""
 
for char in input():
    ascii = ord(char)    #get ascii code
    binary += format(ascii,"07b") #append ascii code

f=lambda l,n:"%s %s "%("0" if l=="1" else "00",n*"0") #Cstyle - this is the shortest as we want to code golf
#f=lambda l,n:f'{("0" if l=="1" else "00")} {(n*"0")} ' #string interpolation
#f=lambda l,n:"{} {} ".format("0" if l=="1" else "00",n*"0") #format function

lastChar, no = binary[0], 1 #loop vars
for i in range(1,len(binary)):
    curChar=binary[i]
    if curChar==lastChar: #continue series if so
        no+=1
    else:
        output+=f(lastChar,no) #convert series to Chuck norris code
        lastChar, no=curChar, 1

output+=f(lastChar,no)

print(output[:-1])