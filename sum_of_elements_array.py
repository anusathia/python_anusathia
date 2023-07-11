n=int(input())
list=[]
for i in range(n):
    list.append(int(input()))
    sum=0
for i in range(len(list)): #1
    sum=sum+list[i] #1+2
print(sum)
