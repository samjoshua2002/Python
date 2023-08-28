import time
n=1000000
start = time.time()
for num in range (1,10):
    print(num, end = ' ')
for num in range (100, n+1):
    nod = 0
    copy_num=num
    sum=0
    while copy_num!=0:
        nod+=1
        copy_num//=10
    copy_num=num
    flag = False
    while copy_num!=0 and flag == False:
        digit = copy_num % 10
        raised_digit = digit ** nod
        sum += raised_digit
        if sum > num:
            flag = True
        copy_num//=10

    if num == sum:
        print(num,end=' ')
end=time.time()
print(end-start)
