text=input()
count=0
while len(text)>0:
    if len(text)==1:
        text=" "
        count=count+1
    else:
        if text[0]==text[1]:
            text=text[2:]
            count=count+1
        else:
            text=text[1:]
            count=count+1
        print(count)                       
