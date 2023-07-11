a=int(input())
b=int(input())
hcf=1
for i in range(1,min(a,b)): #for common minimum no is taken
    if a%i==0 and b%i==0:  
        hcf=i #hcf value is changed for each highest divisor
print(f"the hcf of {a} and {b} is {hcf}")
