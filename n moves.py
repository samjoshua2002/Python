testcase=int(input())
cnt=0
ans=[]
x=0
while cnt<testcase:
    
    y=int(input())
    if x<0:
        z=x+y
        x=z
        ans.append(x)
        cnt=cnt+1
       
    else:
        z=x-y
        x=z
        ans.append(x) 
        cnt=cnt+1
for i in ans:
    print(i)    




     
