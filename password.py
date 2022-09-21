import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMONPQRSTUVWXYZ"
symbol="!@#$%^&<>\/?"
number="1234567890"
s=lower+upper+symbol+number
l=50
password="".join(random.sample(s,l))
print("Password: ",password)