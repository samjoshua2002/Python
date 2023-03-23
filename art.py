word="hello"
for i in range (len(word)):
    print(word[i])
    for j in range(ord("a"),ord(word[i])+1):
        print(chr(j),end="")
    print()
