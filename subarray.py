n = int(input())
sum = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        if arr[i] == sum:
            print("Placed in 1st position")
            break
        else:
            if arr[i] + arr[j] == sum:
                print(i+1, j+1)
