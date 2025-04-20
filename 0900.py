t = int(input())

for _ in range(t):
    k, q, n = map(int, input().split())
    apples = q
    for _ in range(n):
        apples = 2 * (apples + k)
    print(apples)