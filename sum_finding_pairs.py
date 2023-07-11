def pairs(list,sum):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]+list[j]==sum:
                print(list[i],list[j])
list=[0,1,2,3,4,5,2]    
sum=4
pairs(list,sum)