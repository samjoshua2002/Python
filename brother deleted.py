ans=[]
for j in range(int(input())):
    n,k,v=list(map(int,input().split()))
    a=list(map(int,input().split()[:n]))
    #formula=c=v(n+k)-sum of a
    a=sum(a)
    c=v*(n+k)-a
    if c>0 and c%k==0:
        ans.append(int(c/k))
    else:
        ans.append(-1)
for item in ans:
    print(item)            