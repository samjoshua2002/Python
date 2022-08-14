final=[]
for tc in range(int(input())):
    ans=[]
    s=0
    n=int(input())
    goals=list(map(int,input().split()[:n]))
    fouls=list(map(int,input().split()[:n]))
    for j in range(n):
        score=(goals[j]*20)-(fouls[j]*10)
        if score>s:
            ans.append(score)
        else:
            ans.append(0)     
    ans.sort(reverse=True)
    ji=ans[0]
    final.append(ji)
for element in final:
    print(element)    
