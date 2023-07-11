n=int(input())
k=3
for i in range(n):
    for j in range(i+1):
        print(k,end=" ")
        k=k+1
    print()
k=8
for i in range(1,n):
    for j in range(i,n):
        print(k,end=" ")
        k=k-1
    print()