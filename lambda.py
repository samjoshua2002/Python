y=list(map(int,input().split()))
start=int(input())
end=int(input())
print(list(filter(lambda x:x>start and x<end,y)))
