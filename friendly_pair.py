def sum(n): #6
    i=1
    sumof=0
    while i<n: #1<6
        if n%i==0: #6%1==0
            sumof=sumof+i #
        i=i+1
    return sumof
a=int(input()) #6
b=int(input()) #28
sum_a=sum(a)
sum_b=sum(b)
if (sum_a%a)==(sum_b%b):
    print("friendly pair")
else:
    print("not a friendly pair")
