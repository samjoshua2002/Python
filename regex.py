#a12
import re
a='a12b4c10'
s=''
b=re.findall(r'[a-z]',a)
g=re.sub(r'[a-z]',r' ',a)
j=re.findall(r'[1-9]\w*',g)
for i in b:
    for l in j:
        s=s+i*int(l)
print(s)