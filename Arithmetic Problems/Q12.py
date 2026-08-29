num = 1
d = 2
div = []

def divisors(n):
    for i in range(1,n+1):
        if n % i == 0:
            div.append(i)
    return div

while True:
    divisors(num)
    if len(div) <= 500:
        num += d
        d += 1
        div.clear()
    else:
        print(num)
        break

