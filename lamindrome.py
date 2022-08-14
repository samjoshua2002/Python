

# t = int(input())
# for case in range (t):
#     word = input()
#     word = list(word)
#     set1 = set()
#     set2 = set()
#     wordlen = len(word)
#     mid = wordlen//2
#     left = word[:mid]
#     leftTemp = word[:mid]
#     if wordlen%2 == 1:
#         right = word[mid+1:]
#     else:
#         right = word[mid:]
    
#     for i in range (mid):
#         set1.add(left[i])
#         set2.add(right[i])

#     if set1 != set2:
#         print("NO")
#         continue

#     else:
#         for i in left:
#             if i in right:
#                 leftTemp.pop(0)
#                 right.pop(right.index(i))
#             else:
#                 print("NO")
#                 break

#     if leftTemp == right:
#         print("YES")
ans=[]
for i in range(int(input())):
    w=input()
    l=len(w)
    if l%2==1:
        m=l//2
        left=w[:m]
        right=w[m+1:]
        
    else:
        m=l//2
        left=w[:m]
        right=w[m:]
    ansl=list(left)   
    ansr=list(right)     
    ansl.sort()
    ansr.sort()
    if''.join(ansl)==''.join(ansr):
        ans.append("lamindrome")
    else:
        ans.append("not a lamindrome")  
for item in ans:
    print(item)          
