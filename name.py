ans=[]
for i in range(int(input())):
    n=int(input())
    fn=[]
    hn=[]
    for j in range(n):
        name=input()
        fn.append(name)
        hn.append(name.split()[0])
    for k in fn:
        sample = k.split()[0]
        if hn.count(sample)==1:
            ans.append(sample)
        else:
            ans.append(k) 
for l in ans:
    print(l)                   