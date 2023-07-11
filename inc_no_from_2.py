n=int(input())
k=2
for i in range(n):
    for j in range(i+1):
        print(k,end=" ")
        k=k+1
    print()
k=8
for i in range(n):
    count=0
    for j in range(i,n):
        print(k,end=" ")
        k=k+1
        count=count+1
    k=k-(count*2)
    print()

