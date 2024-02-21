n, a, b = int(input()), int(input()), int(input())

if a == b:
    print(n)
else:
    print(n-1)

if a + b >= n:
    print(0)
else:
    print(n - (a+b))
