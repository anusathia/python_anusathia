from math import sqrt
def isPerfectSquare(x):
    if x>=0:
        s=int(sqrt(x)) #if the sqrt is decimal so int should be taken
        print(s)
        return (s*s)==x #if the condition is satisfied,the boolean True comes as output
    return False
n=int(input())
print(isPerfectSquare(n))
if isPerfectSquare(n):
    print("True")
else:
    print("False")
