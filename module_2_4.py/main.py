numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(numbers)
primes=[]
not_primes=[]
for numbers in numbers:
    if numbers == 1:
       continue
    is_primes = True
    for i in range(2, int(numbers)):
        if numbers % i == 0:
            is_primes = False
            break
    if is_primes:
        primes.append(numbers)
    else:
        not_primes.append(numbers)
print(primes)
print(not_primes)











