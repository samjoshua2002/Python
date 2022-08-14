for i in range(int(input())):
    text=input("enter the text to find the holes: ").upper()
    holes='APDRO'
    a=0
    for x in holes:
        a+=text.count(x)
    a+=(2*text.count('B'))
    print(a)
        
