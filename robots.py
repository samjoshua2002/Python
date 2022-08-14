for i in range(int(input())):
    n,x=list(map(int,input().split()))
    s={x}
    string=input()[:n]
    for element in string:
        if element == "r" :
            x=x+1
            s.add(x)
        elif element == "l":
            x=x-1
            s.add(x)
    print(s)
    print(len(s))            
