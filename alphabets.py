known_word=input()
ans=[]
for i in range(int(input())):
    given_word=input()
    assumption=0
    for j in given_word:
        if j in known_word:
            assumption=1
        else:
            assumption=0
            break
    if assumption==1:
        ans.append("yes")
    else:
        ans.append("no")        
for sanjay_black_vishal in ans:
    print(sanjay_black_vishal)
