def sum(no,reverse):
    if no==0:#1234,123,12,1,0
        return reverse,no
    rem=no%10#3
    reverse=reverse*10+rem#reverse=40+3
    return sum(no//10,reverse)#sum(123,4)
no=int(input())
reverse=0
print(sum(no,reverse))