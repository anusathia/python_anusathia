"""vowels=['a','e','i','o','u',"A","E","I","O","U"]
n=input("")
if n in vowels:
    print(n,"is a vowel")
else:
    print(n,"not a vowel")"""
"""n=input()
if 'a'<=n<='z' or 'A'<=n<='Z':
      print("alphabet")
else:
      print("character")"""
"""n=input()
count=0
for i in n:
    count=count+1
print(count)"""
n=input()
a=" "
for i in n:
    i=ord(i)
    if 65<=i<=90:
        i=i+32
        i=chr(i)
    else:
        i=i-32
        i=chr(i)
    a=a+i
print(a)
