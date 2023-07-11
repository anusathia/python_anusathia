n=int(input())
list=[]
for i in range(n):
    list.append(input())
start=0
end=n-1
while(start<end):
    list[start],list[end]=list[end],list[start] #list[end]=10
    start=start+1
    end=end-1
print(list)

