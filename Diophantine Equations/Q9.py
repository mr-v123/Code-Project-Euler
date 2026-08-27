#Edit the code to find the pythagorean triplet (a, b, c) when we know the sum of a, b and c!
Sum = int(input('Enter the sum of a, b and c: '))
for a in range(1, Sum - int(Sum/3)):
    for b in range(a+1, Sum - a):
        if (Sum-a)*(Sum-b) == Sum**2/2:
            c = Sum-a-b
            if a**2 + b**2 == c**2:
                print(a, b, c)