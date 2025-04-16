a, c, k = map(int, input().split())

if k >= c or k > a:
    print(0)
else:
    print((a - k) // c + 1)
