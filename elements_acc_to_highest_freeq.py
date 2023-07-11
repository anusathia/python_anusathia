a=list(map(int,input().split()))
count1=[]
elt=[]
for i in range(len(a)):
    count=0
    if a[i]!=" ":
        elt.append(a[i])
        for j in range(len(a)):
            if i!=j:
                if a[i]==a[j]:
                    count=count+1
                    a[j]=" "
        count1.append(count)
print(elt)
print(count1)
n=len(count1)
#des
for i in range(len(count1)):
    for j in range(i+1,len(count1)):
        if count1[i]<count1[j]:
            count1[i],count1[j]=count1[j],count1[i]
            elt[i],elt[j]=elt[j],elt[i]
print(count1)
print(elt)
#printing the elements
output=[]
for i in range(n):
        
    s=(count1[i]+1)*str(elt[i])
    s=int(s)
    l=0
    while(s!=0):
        l=s%10
        print(l,end=" ")
        s=s//10

        

