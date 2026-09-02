def lcs(n):
    l = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        l += 1
    return l

l = 0
ans = 0
for i in range(1, 1000000):
    length = lcs(i)
    if length > l:
        l = length
        ans = i
print(ans, l)