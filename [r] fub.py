def getallpos(findstr,tofind):
    opos=0
    allpos=[]
    while True:
        if tofind in findstr:
            pos=findstr.index(tofind)
            opos+=pos
            allpos.append(opos)
            findstr=findstr[pos+1:]
        else:
            break
    print(allpos)
getallpos(input("Enter the letter: "),input("To find: "))
