testcase=int(input())
cnt=0
answers=[]
while cnt<testcase:
    friends=int(input())
    recommendation=list(map(int,input().split()[:friends]))
    md={}
    for item in recommendation:
        md[item]=md.get(item,0)+1
    y=sorted(md.items(),key=lambda x:x[1],reverse=True)
    if len(y)>1:
        if y[0][1]==y[1][1]:
            answers.append("confused")
        else:
            answers.append(y[0][0])
    else:
        answers.append(y[0][0])
    cnt+=1
for x in answers:
    print(x)
