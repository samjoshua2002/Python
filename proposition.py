a,b,c,d=list(map(int,input().split()[:5]))
if(a/b==c/d):
    print("possible")
elif(c/a==b/d):
    print("possible")
elif(b/a==c/d):
    print("possible")
elif(a/c==b/d):
    print("possible")
else:
    print("not possible")            