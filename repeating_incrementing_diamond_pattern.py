n=int(input())
k=2
for i in range(n):
    for j in range(i+1):
        print(k,end=" ")
    k=k+1
    print()
k=5
for i in range(n):
    for j in range(i,n):
        print(k,end=" ")
    k=k-1
    print()