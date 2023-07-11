a=int(input())
org=a
def divisors(a):
    i=1
    while i<a:#1<=28
        if a%i==0:#28%1
            divisors_list.append(i)
        i=i+1
divisors_list=[]
divisors(a)
print(divisors_list)  
sum=0 
for i in range(len(divisors_list)):
    sum=sum+divisors_list[i]
    print(sum)
if(sum==org):
    print("perfect no")
else:
    print("not a perfect no")
