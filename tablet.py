for i in range(int(input())):
    n,b=list(map(int,input().split()))
    case=0
    app=[]
    while case<n:
        w,h,p=list(map(int,input().split()))
        if p<=b:
            a=w*h
            app.append(a)
            case=case+1   
        else:
            app.append(0) 
            case=case+1
    app.sort(reverse=True)
    if app[0]==0:
        print('No Tablets')
    else:    
        print(app[0])

      
        