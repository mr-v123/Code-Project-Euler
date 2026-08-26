def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

rank = 0
for k in range(2, 1000000):
    if isPrime(k):
        rank += 1
        if rank == 10001:
            print(k, rank)
            break
        