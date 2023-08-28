num=1634
nod = 0
copy_num=num
sum=0
while copy_num!=0:
    nod+=1
    copy_num//=10
copy_num=num
print("nod" , nod)
while copy_num!=0:
    digit = copy_num % 10
#digit to the power of nod
    raised_digit = digit ** nod
    sum += raised_digit
#    print(digit, raised_digit, sum)
    copy_num//=10

if num == sum:
    print("Arms")
else:
    print("Not Arms")
