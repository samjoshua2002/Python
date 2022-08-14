txt=input()
result=" "
for pos in range(len(txt)):
    if txt[pos].islower():
        result+=txt[pos].upper()
    elif txt[pos].isupper():
        result+=txt[pos].lower() 
    else:
        result+=txt[pos]
print(result)

           
