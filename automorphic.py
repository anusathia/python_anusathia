a=input()#76
a_len=len(a)
a=int(a)
s=a*a #5776
s=str(s)
#s[-2::]=76 
print(a)
if (s[-a_len::]==str(a)): 
    print("automorphic")
else:
    print("not automorphic")
