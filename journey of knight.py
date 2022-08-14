ans=[]
for i in range(int(input())):
    x1,y1,x2,y2=map(int, input().split())
    a=abs(x1-x2)
    b=abs(y1-y2)
    if (a+b)%2==0:
        ans.append("YES")
    else:
        ans.append("NO")
for j in ans:
    print(j)        