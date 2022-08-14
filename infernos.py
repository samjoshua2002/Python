ans=[]
for i in range(int(input())):
    n,t=list(map(int,input().split()[:2]))
    health=(list(map(int,input().split()[:n])))
    st=n
    c=sum(health)
    counter=0
    while c>0:
        for j in range(len(health)):
            if health[j]!=0:
                health[j]=health[j]-1
        c=sum(health) 
        counter=counter+1       
        

    m=min(st,counter)   
    ans.append(m)         
for hj in ans:
    print(hj)