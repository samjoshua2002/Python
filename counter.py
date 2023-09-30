from collections import Counter
from operator import itemgetter
x=[]
i=str(int(input()))

for j in i:
    x.append(j)
c=Counter(x)
print(c)
s = dict(sorted(c.items(), key=itemgetter(1), reverse=True))
for key,value in s.items():
    z=str(key)
    print(z*value,end="")


    