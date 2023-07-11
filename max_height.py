number=input("enter list of numbers")
number_list=number.split()
count=0
for i in range(0,len(number_list)):
    number_list[i]=int(number_list[i])
maximum_number=number_list[0]
for number in number_list:
    if number>maximum_number:
        maximum_number=number
print(maximum_number)