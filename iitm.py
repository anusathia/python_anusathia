l=list(input().split())
n=input()
count=0
for i in range(len(l)):
    if n in l[i]:
        count=count+1
if count==0:
    print("NO")
else:
    print("YES")
    print(count)




