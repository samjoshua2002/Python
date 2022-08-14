from ast import While
from typing import Counter


a=int(input("Enter overall amount"))
b=int(input("enter no of users"))
counter = 0
while counter<b :
    c=int(input())
    if c<=a:
        print("successfully withdraw amount!")
        a=a-c
    else:
        print("Insufficient amount")
counter=counter+1        


