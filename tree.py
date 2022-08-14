ans=[]
for i in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()[:n]))
    ans.append(len(x)-(0 in x))
for item in ans:
    print(item)  