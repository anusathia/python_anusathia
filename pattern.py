n=int(input()) #4
k=3
for i in range(n): #1,2,3
    for j in range(i+1):
        print(k,end=" ")
        k=k+1
    print() 
k=6                     
for i in range(1,n):
    for j in range(i,n):
        print(k,end=" ")
        k=k+1
    k=6-i-1
    
    print() #0,1,2,3
        