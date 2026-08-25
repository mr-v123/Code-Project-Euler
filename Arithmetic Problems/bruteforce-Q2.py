u1 = 1
u2 = 2
un = u1 + u2
S = 0
while un <= 4000000:
    u1 = u2
    u2 = un
    un = u1 + u2
    if un % 2 == 0:
        S += un
print(S+2)