ans=[]
for i in range(int(input())):
    tlimak,tbob=list(map(int,input().split()))
    limak=0
    bob=0
    candies=1
    while True:
        if candies%2==1:
            if limak+candies<= tlimak:
                limak=limak+candies
            #shift+tab
            else:
                ans.append('bob ')
                break
        else:
            if bob+candies<=tbob:
                bob=bob+candies
            else:
                ans.append('limak')
                break
        candies=candies+1
cnt=0
while cnt<len(ans):
    print(ans[cnt])
    cnt=cnt+1   



              
