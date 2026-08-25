def isPalindrome(s):
    good = 1
    n = 0
    while n <= int(len(s)/2) and good ==1:
        if not s[n] == s[-(n+1)]:
                good = 0
        n += 1
    return good

ans = 0
for a in range(100, 1000):
     for b in range(100, 1000):
          if isPalindrome(str(a*b)):
               if a*b > ans:
                    ans = a*b

print(ans)