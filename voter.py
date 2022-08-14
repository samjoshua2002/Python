x,y,z=list(map(int,input().split()[:4]))
mylist=[]
final=[]
for i in range(x):
    xlist=int(input())
    mylist.append(xlist)
for j in range(y):
    ylist=int(input())
    mylist.append(ylist)
for k in range(z):
    zlist=int(input())
    mylist.append(zlist) 
myset=set(mylist)       
for item in myset:
    if  mylist.count(item)>=2:
        final.append(item)
print(len(final))
for het in final:
    print(het)   

