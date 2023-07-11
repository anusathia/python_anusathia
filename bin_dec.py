"""bin=int(input())
dec=0
i=0
while(bin>0): #1
    l=bin%10 #1
    dec=dec+l*(2**i) #0+1*2^1
    i=i+1 #1
    bin=bin//10 #1
print(dec)"""
n=8
print(bin(n)[2:])