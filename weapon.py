n=int(input("enter no of soldiers :"))
countereven=0
counterodd=0
for i in range(n):
    w=int(input())
    if w%2==0:
        countereven=countereven+1
    else:
        counterodd=counterodd+1
if countereven>counterodd:
    print("Ready to battle")
else:
    print("not ready")    

