# ans=set()
# v=[]
# for _ in range(int(input())):
#     n=int(input())
#     a=list(map(int,input().split()[:n]))
#     for j in range(1,n):
#         if a[j]!=a[j-1]:
#             ans.add(j)
#             ans.add(j-1)
# l=len(ans)
# v.append(l)
# for item in v:
#     print(item)
# ctrl+/
for i in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    s = set()
    for i in range(1, N):
        if(A[i] != A[i-1]):
            s.add(i)
            s.add(i-1)
    print(len(s))    