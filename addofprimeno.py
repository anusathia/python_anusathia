prime_list=[]
n=int(input())
count=0
j=2
while(j<n):#2<30
    for i in range(1,j+1):
        if j%i==0: 
            count=count+1
    if count==2:
        prime_list.append(j)
    count=0
    j=j+1
print(prime_list)
for x in range(len(prime_list)):#2,15
    for i in range(x+1,len(prime_list)):#2,3,5,7,11 for 2nd recurssion 3,13
        if prime_list[x]+prime_list[i]==n:#2+3/5/7/11 for 2nd recursion 3+5
            print(prime_list[x],prime_list[i])
        
        
    






           