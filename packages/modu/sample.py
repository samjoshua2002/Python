
n = int(input())
a=list(map(int,input().split()[:n]))
myset=set(a)
mylist=list(myset)
mylist.sort(reverse=True)
print(mylist[1])
