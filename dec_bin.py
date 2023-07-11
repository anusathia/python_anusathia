def convertBinary(num):
    binaryArray = []
    while num>0:
        binaryArray.append(num%2) 
        print(num%2)
        print(binaryArray)
        num = num//2
        print(num)
    for j in binaryArray:
        print(j, end="")


decimal_num = 21
convertBinary(decimal_num)