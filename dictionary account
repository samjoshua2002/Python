k=list(map(str,input().split()))
v=list(map(int,input().split()))
dictionary={k[i]:v[i] for i in range(len(k))}
print(dictionary)

for i in range(int(input("Enter no of time the program need to run: "))):
    print("\n")
    id=input('Enter customer id: ')
    if id in k:
        v=dictionary.get(id)
        amount=int(input('Enter withdraw amount: '))
        if v>=amount:
            change=v-amount
            dictionary[id]=change
            print("Available amount",change)
            print("\n")
        else:
            print("Insufficient Amount")
            print("\n") 
    else:
        print("Wrong Account") 
                