n, q = map(int, input().split())
a = list(map(int, input().split()))[:n]
b = list(map(int, input().split()))[:n]

for i in range(q):
    a0 = 0
    b0 = 0
    s = 0
    l,r = map(int, input().split())
    for i in range(l-1,r):
        a0 += a[i]
        b0 += b[i]
        s += a0 if a0>b0 else b0
    print(s)

