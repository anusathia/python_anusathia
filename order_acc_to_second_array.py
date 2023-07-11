def checkorder(a,b):
    a_sort=[]
    b_sort=[]
    for i in range(len(b)):
        count=0
        for j in range(len(a)):
            if a[j]!=" ":
                if a[j]==b[i]:
                        a_sort.append(a[j])
                        a[j]=" "
                count=count+1
    print(a)
    print(a_sort)
    for i in range(len(a)):
        if a[i]!=" ":
             a_sort.append(a[i]) 
        
    print(a_sort)







a=list(map(int,input().split()))
b=list(map(int,input().split()))
checkorder(a,b)