n, a, b = map(int, input().split())

if a == 100:
    if b == 100:
        result = n
    else:
        result = 0.0
else:
    result = n * (100 - a) / (100 - b)

print("{0:.5f}".format(result))
