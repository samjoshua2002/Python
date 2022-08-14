txt=input()
s=0
k=0
for y in range(len(txt)):
    for x in range(len(txt)-y):
        st=txt[x:x+y+1]
    if st[0] in 'aeiou':
        k+=1