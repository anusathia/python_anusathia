n=int(input())
list=[]
for i in range(n):
    list.append(input())
print(list)
pal_list=[]
def palindrome(list):
    for i in range(n):
        new=list[i]
        if new[::-1]==new:
            pal_list.append(new)
palindrome(list)
print(pal_list)
def des(pal_list,a,b):
    max=0
    for i in range(a,b):
        for j in range(a+1,b):
            if int(pal_list[i])<int(pal_list[j]): #11,10,44,45
                max=pal_list[j]
    return max
output=des(pal_list,0,len(pal_list))
print(output)



 

