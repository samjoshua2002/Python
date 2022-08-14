from tkinter.tix import TEXT


testcase=int(input())
cnt=0
ans=[]
while cnt<testcase:
    n,i=list(map(int,input().split()))
    x=list(map(TEXT,input().split()[:n+1]))