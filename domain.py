ans=[]
from collections import Counter
for i in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()[:n]))
    c=Counter(x)
    v=list(c.values())
    if len(set(x))==1:
        ans.append("Yes")
    elif len(set(x))==len(x):
        ans.append("No")
    else:
        m=max(v) 
        cm=v.count(m) 
        if cm>1:
            ans.append("N0")
        else:
            ans.append("Yes")      
for rubesh_sanjay in ans:
    print(rubesh_sanjay)
    

