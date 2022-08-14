testcase=int(input())
cnt=0
ans=[]
while cnt<testcase:
    x=int(input())
    s=0.143
    y=(s*x)**x
    z=round(y)
    ans.append(z)
    cnt=cnt+1
for i in ans:
    print(i)    