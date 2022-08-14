t=int(input("Enter no of testcase: "))
counter=0
for i in range(t):
   w=int(input("enter no of women: "))
   for j in range(w):
      a=int(input("ages: "))
      if a>18:
        counter=counter+1
        print("THE NO OF WOMENS CAN BE SELECTED",counter)
      else:
        print("Not eligible")
