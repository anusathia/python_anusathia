def asc(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a
def duplicants(x):
    b=[] 
    for i in range(len(x)):
        count=0
        if x[i]!=" ":
            for j in range(len(x)):
                if i!=j:
                    if x[i]==x[j]:
                        count=count+1
                        x[j]=" "
                        if count==1:
                            b.append(x[i])
            if count==0 :
                b.append(x[i])
    return b
b=[]
a=list(map(int,input().split()))
print(a)
lista=asc(a)
list_a=duplicants(lista) #have to remove duplicants
print(list_a)
c=list(map(int,input().split()))
print(c)
listc=asc(c)
print(listc)
list_c=duplicants(listc)
print(list_c)


