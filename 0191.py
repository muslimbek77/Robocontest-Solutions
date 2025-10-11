MOD = 1234567

T = int(input())  # testlar soni
for _ in range(T):
    N = int(input())  # shaharlar soni
    roads = list(map(int, input().split()))  # N-1 ta son
    result = 1
    for a in roads:
        result = (result * a) % MOD
    print(result)
