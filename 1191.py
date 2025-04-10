n, m, k, d = map(int, input().split())

time_bus = d + n * m
time_walk = n * k
min_time = min(time_bus, time_walk)

if k > m:
    denominator = k - m
    i_min = (d + denominator - 1) // denominator
    if i_min <= n:
        for i in range(i_min, n + 1):
            current_time = i * k + (n - i) * m
            if current_time < min_time:
                min_time = current_time

print(min_time)