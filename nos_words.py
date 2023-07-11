ones_list=[' ','one','two','three','four','five','six','seven','eight','nine']
tens_list=[' ','ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
n=input() #1121
loft=n
len_loft=len(loft)
word=''
if len_loft==4:
    word=word+(ones_list[int(loft[0])])+" "+"thousand"+" "
    print(word)
    word=word+(ones_list[int(loft[1])])+" "+"hundred"+" "
    print(word)
    word=word+tens_list[int(loft[2])]+" "
    print(word)
    word=word+ones_list[int(loft[3])]+" "
    print(word)
if len_loft==3:
    word=word+(ones_list[int(loft[0])])+" "+"hundred"+" "
    print(word)
    word=word+tens_list[int(loft[1])]+" "
    print(word)
    word=word+ones_list[int(loft[2])]+" "
    print(word)
if len_loft==2:
    word=word+tens_list[int(loft[0])]+" "
    print(word)
    word=word+ones_list[int(loft[1])]+" "
    print(word)
if len_loft==1:
    word=word+ones_list[int(loft[0])]+" "
    print(word)



     