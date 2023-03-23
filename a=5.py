for i in range (int(input ())):
    n=int(input("no of persons "))
    m=int(input("first to be served "))
    person=list(range (1,n+1))
    a=n-m
    k=person [a:]
    del person [a:]
    person=k+person
    print (person)