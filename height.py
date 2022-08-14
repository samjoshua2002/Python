testcase=int(input())
cnt=0
ans=[]
while cnt<testcase:
    x,y=list(map(int,input().split()[:3]))
    while x!=y:
        if x>y:
            ans.append("A")
        else:
            ans.append("B")
        break
    cnt=cnt+1    
for i in ans:
    print(i)    
