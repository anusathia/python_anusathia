a=list(map(int,input().split()))
b=list(map(int,input().split()))
count=0
for i in a:
    for j in b:
        if i==j:
            count=count+1
if count==0:
    print("disjoint")
else:
    print("not a disjoint")