def  fact(a,facti):#6,1 5,6 30,4
    if a==0:
        return facti
    facti=facti*a#1*6 120
    return fact(a-1,facti)#5 4
a=int(input())
facti=1
print(fact(a,facti))
