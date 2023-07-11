
def factors(n):
    i=1
    while i<=n:
        if n%i==0:
            print(i,end=" ")
        i=i+1

n=int(input())
print(f"the factors of {n} are ")
factors(n)