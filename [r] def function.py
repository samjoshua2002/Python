a=[]                                                                      #Empty list
for i in range(int(input("Testcase : "))):                                #Testcase
    print("                   MINIMUM AND MAXIMUM                   ")
    def nmax(mylist,findmax=1):                                           #Max function
        newlist=list(set(mylist))
        if findmax<=len(mylist):
            newlist.sort(reverse=True)
            a.append("Maximum-"+ str(newlist[findmax-1]))
        else:
            return 0
    def nmin(mylist,findmin=1):                                           #Min function
        newlist=list(set(mylist))
        if findmin<=len(mylist):
            newlist.sort()
            a.append('Minimum-'+str(newlist[findmin-1]))
        else:
            return 0
    print('Which operation to be performed')                              #comments
    print("1-(Maximum n numbers) ")                                       #comments
    print("2-(Minimum n numbers) ")                                       #comments
    n=int(input())
    if n==1:
        nmax(list(map(int,input("list ").split())),int(input("max ")))
    elif n==2:
        nmin(list(map(int,input("list ").split())),int(input("min ")))
    else:
        print("Invalid Try Again")
for j in a:                                                              #display elements in empty list
    print(j)        