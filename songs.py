n=int(input())
songslist=list(map(int,input().split()[:n]))
k=int(input())
song=songslist[k-1]
songslist.sort()
print(songslist.index(song)+1)
