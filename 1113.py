N, K = map(int, input().split())
result = 0
while N:
    result += N % K
    N = N//K
print(result)