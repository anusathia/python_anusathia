def asc(arr,a,b):
    for i in range(a,b):
        for j in range(i+1,b):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
def dec(arr,a,b):
    for i in range(a,b):
        for j in range(i+1,b):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print(arr)
asc(arr,0,n//2)
print(arr)
dec(arr,n//2,n)
print(arr)




