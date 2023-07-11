size=input("what size pizza you eant(S/M/L)")
bill=0
if size=='S' or size=='s':
    bill+=100
    print("small pizza price is 100 rs")
elif size=='M' or size=='m':
    bill+=200
    print("medium pizza price is 200 rs")
elif size=='L' or size=='l':
    bill+=200
    print("large pizza price is 300 rs")

add=input("do u want to add peporani(Y/N)")
if add=="Y" or add=='y':
    if size=='s' or size=='S':
        bill+=30
    if size=='m' or size=='M' or size=='l' or size=='L':
        bill+=50
print(f"your final bill is {bill}")