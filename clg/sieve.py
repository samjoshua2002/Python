import time

start = time.time()
range_  = 10000000
numbers = [True for _ in range(range_)]
#print(numbers)
numbers[0] = False
numbers[1] = False
prime = 2
composite_ctr = 2
multiple = 4

while multiple < range_:
    numbers[multiple] = False
    multiple += prime
prime = 3
while prime * prime <= range_:
    if numbers[prime] == True:
        multiple = prime * prime
        inc = 2 * prime

        while multiple < range_:
                numbers[multiple] = False
                multiple += inc
    prime += 1


#print(len(list(filter(lambda x : x == True, numbers))))
print(numbers.count(True))
#prime_ctr = range_ - composite_ctr
"""
prime_ctr=0
for res in numbers:
    if res == True:
        prime_ctr += 1
"""
end = time.time()
#print(prime_ctr)
print(end-start)
