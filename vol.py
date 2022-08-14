a=int(input("initial volume"))

b=int(input("SET TO"))
if a>b:
    c=a-b
    print(c)
else:
    c=b-a
    print("-",c)        