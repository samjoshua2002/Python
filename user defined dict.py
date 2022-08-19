for i in range(int(input("Enter no of time the program need to run: "))):
    k=list(map(int,input().split()))
    v=list(map(str,input().split()))
    dictionary={k[i]:v[i] for i in range(len(k))}
    print(dictionary)
    def access(n):
        if n in k:
            v=dictionary.get(n)
            print(v)
        else:
            print("Key not exist")  
    n=int(input("Enter the Key Value: "))    
    access(n)    