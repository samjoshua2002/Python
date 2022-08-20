x=list(map(int,input("Enter two numbers to multiply: ").split()[:2]))
a=x[0]*x[1]
print("The product of {}×{}={}".format(x[0],x[1],a))