h=[]
for i in range(int(input())):
    a,b,c,d,e=list(map(int,input().split()))

    if (a+b<=d and c<=e) or (b+c<=d and a<=e) or (c+a<=d and b<=e) :
        h.append("yes")
    else:
        h.append("no")

listcounter=0        
while listcounter<len(h):
    print(h[listcounter])
    listcounter=listcounter+1

