t=int(input())
dict={}
ans=[]
for t in range(t):
    name=input()
    grade=float(input())
    dict[name]=grade
grades=set(dict.values())
grades.remove(min(grades))
x=min(grades)
for key,value in dict.items():
    if value==x:
        ans.append(key)
sort=sorted(ans)        
for i in sort:
    print(i)    