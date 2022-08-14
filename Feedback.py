ans=[]
for i in range(int(input())):
    a=input()
    b="101"
    c="010"
    if b in a or c in a:
        ans.append('Good')
    else:
        ans.append('Bad')
for j in ans:
    print(j)         