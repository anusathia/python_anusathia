import random
names=input("enter name seperated by commas:")
list=names.split(",")
print(list)
len_list=len(list)
choice=random.randint(0,len_list-1)
print(f"{list[choice]} willpay the bill")

