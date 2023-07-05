def reverse(a):
    result=""
    for i in a:
        result=i+result
    return(result)
s=input()

a=reverse(s)
print("the reverse of the string is: ",a)


'''
s = "intelli"
result ="".join(reversed(s))
print(result)

'''