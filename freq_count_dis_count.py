"""n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print(arr)
count={}
for i in arr:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
        print(count[i])
for key,value in count.items():
    print(key,"=",value)"""
a=list(map(int,input().split()))
print(a)
b=[]
for i in range(len(a)):
    count=0
    c=[]
    if a[i]!=" ":
        for j in range(len(a)):
            if i!=j:
                if a[i]==a[j]:
                    count=count+1
                    a[j]=" "
        if count>0:
            b.append(a[i])
print(b)




    