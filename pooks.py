testcase=int(input())
cnt=0
ans=[]
while cnt<testcase:
    n=int(input())
    if n==2 or n==3:
        ans.append(n-1)
    else:
        ans.append(n)
    cnt=cnt+1
for i in ans:
    print(i)            