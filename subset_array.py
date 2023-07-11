arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
count=0
for j in arr2:
    if j in arr1:
            count=count+1
if count==len(arr2):
    print("arr2 is  a subset of arr1")
else:
    print("arr2 is not  a subset of arr1")