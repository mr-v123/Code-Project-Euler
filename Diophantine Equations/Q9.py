#a+b+c = 1000 and a^2 + b^2 = c^2 => (1000-a)(1000-b) = 500000, a+b < 667
for a in range(1, 667):
    for b in range(1, 667-a):
        if (1000-a)*(1000-b) == 500000:
            c = 1000-a-b
            if a**2 + b**2 == c**2:
                print(a*b*c)