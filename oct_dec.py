bin=int(input())
dec=0
i=0
while(bin>0): #1
    l=bin%10 #1
    dec=dec+l*(8**i) #0+1*8^1
    i=i+1 #1
    bin=bin//10 #1
print(dec)