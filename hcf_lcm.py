a=int(input())
b=int(input())
hcf=1
for i in range(1,min(a,b)): #for common minimum no is taken
    if a%i==0 and b%i==0:  #24%3 and 15%3
        hcf=i #hcf value is changed for each highest divisor
print(f"the hcf of {a} and {b} is {hcf}")

for i in range(max(a,b),1+(a*b)): #24,1+(24*15)=360
    if i%a==i%b==0: #120%24==120%15
        lcm=i 
        break
print(f"LCM of {a} and {b} is {lcm}")

