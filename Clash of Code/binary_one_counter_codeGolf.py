for i in range(int(input())):
    binaryString = bin(int(input()))
    counter =0
    for i in binaryString[2:]:
        if i == "1":
            counter +=1
    print(counter)
