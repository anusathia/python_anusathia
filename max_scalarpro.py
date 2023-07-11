def asc(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a
def scalarpro(lista,listc):
    sum=0
    for i in range(len(lista)):
        sum=lista[i]*listc[i]+sum
    print(sum)

a=list(map(int,input().split()))
print(a)
lista=asc(a)
print(lista)
c=list(map(int,input().split()))
print(c)
listc=asc(c)
print(listc)
if len(lista)== len(listc):
    scalarpro(lista,listc)

elif len(listc)>len(lista):
    equi=len(c)-len(a)
    for i in range(equi):
        lista.append(int('0'))
    scalarpro(lista,listc)

elif len(lista)>len(listc):
    equi=len(a)-len(c)
    for i in range(equi):
        listc.append(int('0'))
    scalarpro(lista,listc)





