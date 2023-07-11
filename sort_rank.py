store=list(map(int,input().split()))
print(store)
n1=store.copy()
for i in range(len(n1)):
        for j in range(i+1,len(n1)):
            if n1[i]>n1[j]:
                n1[i],n1[j]=n1[j],n1[i]
print(n1)
print(store)
for i in range(len(store)):
    for j in range(len(n1)):
        if store[i]==n1[j]:
            store[i]=j+1
print(store)
     