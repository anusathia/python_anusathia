n=input("Enter number")
str=""
for i in range(len(n)):
    if n[i]=="0":
        str=str+"1"
    else:    
        str=str+n[i]
print(str)

