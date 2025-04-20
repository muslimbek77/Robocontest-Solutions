n = int(input())
r = []
c = [0] * n
t = 0
for _ in range(n):
    w = list(map(int, input().split()))
    s = sum(w)
    r.append(s)
    t += s
    for j in range(n):
        c[j] += w[j]
max_sum = max(max(r), max(c))
print(n * max_sum - t)