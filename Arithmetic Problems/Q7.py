def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    rank = 0
    k = 1
    while rank < 10001:
        k += 1
        if isPrime(k):
            rank += 1
            if rank == 10001:
                print(rank, 'prime number is: ', k)
                break
