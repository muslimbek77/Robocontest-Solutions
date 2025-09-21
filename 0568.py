M, N = map(int, input().split())
cnt = [0] * (M + 2)  # M+1 gacha kerak, +1 buffer

for _ in range(N):
    a, b = map(int, input().split())
    cnt[a] += 1
    cnt[b+1] -= 1

cur = 0
for i in range(1, M+1):
    cur += cnt[i]
    if cur != 1:
        print(i, cur)
        break
else:
    print("OK")
