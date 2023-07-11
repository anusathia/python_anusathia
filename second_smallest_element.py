def smallest(list):
    min=list[0]
    for i in range(n):
        if list[i]<min:
            min=list[i]
    return min
n=int(input("Enter the no of elements in an array"))
list=[]
for i in range(n):
    list.append(int(input()))
min=smallest(list)
min_index=list.index(min)
print(min_index)
list[min_index]=1000
second=smallest(list)
print(second)


