def findpairs(list):
    s=set()
    for (x,y) in list:
        s.add((x,y))
        if (y,x) in s:
            print((x,y))

list=[(1,2),(2,1),(4,5)]
findpairs(list)