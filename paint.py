ans=[]
for tc in range(int(input())):
    n=int(input())
    count=0
    colour=input()[:n]
    a=colour.count("R")
    b=colour.count("G")
    c=colour.count("B")
    m=max(a,b,c)  
    ans.append(len(colour)-m)       
for item in ans:
    print(item)
