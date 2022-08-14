tc=int(input())
ans=[]
for tt in range(tc):
    n=int(input())
    stones=list(map(int,input().split()[:n]))
    turn="chef"
    if 1 in stones:
        turn="chefina"
    else:
        while True:
            stones.sort()
            if stones[i]>2:
                stones[i]-=1
                if turn== "chef":
                    turn="chefina"
                else:
                    turn== "chef"
                break
            else:
                break
    if turn=="chef":
        ans.append("chefina")
    else:
        ans.append("chef")
for x in ans:
    print(x)
                    
                
