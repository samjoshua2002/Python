start = 10
last = 15
res=0
for num in range(start, last+1):
    num = str(num)
    flags = []
    for ctr in range (0,10):
        flags.append(0)
    for char in num :
        flags [  int(char) ] +=1
    print(flags)
    duplicateFlag = False
    for ctr in range(0,10):
        if flags[ctr] > 1:
            duplicateFlag = True
    if duplicateFlag == False:
        res+=1
print(res)
   '''
    for flag in flags:
        if flags [ flag ] > 1:
            duplicateFlag=True
            '''
 
