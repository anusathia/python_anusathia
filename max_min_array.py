n=int(input("enter the no of elements in an array"))
list=[]
for i in range(n):
    list.append(int(input()))
print(list)
min=list[0]
for i in range(n): #0,1,2,3
    if list[i]<min: #1>2
        min=list[i]
print(min)
max=list[i]
for i in range(n): #0,1,2,3
    if list[i]>max: #1>2
        max=list[i]
print(max)
       
