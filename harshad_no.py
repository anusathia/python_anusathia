a=int(input())
g=a
sum=0
while(a!=0):
    l=a%10
    sum=sum+l
    a=a//10
if (g%sum==0):
    print("harshad no")
else:
    print("not a harshad no")