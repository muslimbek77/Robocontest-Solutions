t = int(input())
for _ in range(t):
    n = int(input())
    q, r = divmod(n, 9)
    if r != 0:
        print(r)
    else:
        print(9)