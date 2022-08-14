ans=[]
for i in range(int(input())):
    coins=int(input())
    row=1
    while True:
        c=(row*(row+1))/2
        if c==coins:
            ans.append(row)
            break
        else:
            row+=1
for j in ans:
    print(j)