def factorial(x):
    fact=1
    while(x!=0):
        fact=fact*x
        x=x-1
    return fact
n=int(input("Enter the no of people"))
r=int(input("Enter the no of seats in a classroom"))
nr=factorial(n)
p=(n-r)
dr=factorial(p)
print("the total no of ways is")
print(int(nr/dr))