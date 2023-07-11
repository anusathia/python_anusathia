def hcf(x,y):
    hcfe=1
    for i in range(1,min(x,y)+1):
        if x%i==0 and y%i==0:
            hcfe=i
    return hcfe


nr1=int(input("Enter numerator and denominator of first number:"))
dr1=int(input())
nr2=int(input("Enter numerator and denominator of second number:"))
dr2=int(input())
sum1=dr2*nr1
sum2=dr1*nr2
total=sum1+sum2
lcm=dr1*dr2
print(total)
print(lcm)
mass=hcf(total,lcm)
print(mass)
frac1=int(total/mass)
frac2=int(lcm/mass)
print(f"{nr1}/{dr1}+{nr2}/{dr2}={frac1}/{frac2}")

