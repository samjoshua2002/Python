phoneNumber = 9442161065
phoneNumber = str(phoneNumber)
words_digit = ['Zero ', 'One ', 'Two ','Three ','Four ','Five ','Six','Seven ','Eight ','Nine']
for char in phoneNumber :
    #print(char)
    print( words_digit[int(char)] , end=' ')
