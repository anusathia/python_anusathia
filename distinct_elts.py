n=int(input())
list=[]
for i in range(n):
    list.append(int(input()))
print(list)
count=0
 #10,20,10
for i in range(n):
    new=list[i]
    if new!=' ':
        for j in range(0,n):
            if i!=j:
                if new==list[j]:
                    list[j]=' '
                    list[i]=new=" "
print(list)
for i in range(n):
    if list[i]!=' ':
        count=count+1
print(count)