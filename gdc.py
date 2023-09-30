
a, b = list(map(int, input().split()))[:2]

while(b>0):
    t=b
    b=a%b
    a=t
print(a)    

