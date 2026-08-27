from Q7 import isPrime

Sum = 0
for i in range(1, 2000000):
    if isPrime(i):
        Sum += i
print(Sum)