testcase=int(input())
case=0
while case<testcase: 
    n,k=list(map(int,input().split()))
    case1=0
    s=0
    ans=[]
    while case1<n:
        t,d=list(map(int,input().split()))
        if k>t:
            k-=t
        else:
            s = s + (t-k)*d
            k = 0
        case1=case1+1 
    case=case+1         
    ans.append(s)            
    listcounter=0        
    while listcounter<len(ans):
        print(ans[listcounter])
        listcounter=listcounter+1

    