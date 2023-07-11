def factors(n):
    i=1
    while i<=n:
        if n%i==0:
            prime(i)
        i=i+1
def prime(i):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count==2:
        print(i,end=" ")
    count=0
n=int(input())
factors(n)
        
    
    