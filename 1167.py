def min_contests(N):
    # 5 ta contestlar sonini maksimal qilib olishga harakat qilamiz
    y = N // 5
    while y >= 0:
        remaining = N - 5 * y
        if remaining % 3 == 0:
            x = remaining // 3
            return x + y
        y -= 1
    return -1

# Input
N = int(input())
print(min_contests(N))