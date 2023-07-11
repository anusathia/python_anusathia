a=int(input("Enter a number"))
original=a
strong=0
def factorial(i):#5
    fact=1
    while(i!=0):#5
        fact=fact*i#1*5
        i=i-1#4
    return fact
while(a!=0):#14
    i=a%10 #4
    strong=strong+factorial(i)#5!+fact(4)
    a=a//10
print(strong)
if (strong==original):
    print("strong")
else:
    print("not a strong no")



