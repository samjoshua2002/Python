p=[]
for i in range(int(input())):
    v=[]
    n,x=list(map(int,input().split()))
    for j in range(n):
        s,r=list(map(int,input().split()))
        if x>=s and s>=0:
            v.append(r)
            s=s-1
    b=max(v)  
    p.append(b) 

w=len(p)
for k in range(w):
    print(p[k])