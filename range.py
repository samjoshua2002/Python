ans=[]
for rubesh in range(int(input())):
    n,x=list(map(int,input().split()))
    if n>=x:
        ans.append(x)
    else:
        while x>n:
            x=x-n-1
            ans.append(x)    
for rubesh in ans:
    print(rubesh)        