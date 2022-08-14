x=list(map(int,input().split()[:6]))
for i in range(len(x)-1):#to twice the list
    x[i]=x[i]*x[-1]  
if sum(x[:-1])>120:
    print("yes")
else:
    print("no")
