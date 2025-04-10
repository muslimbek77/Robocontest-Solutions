n, m, k, d = map(int, input().split())
time_bus = d + n * m
time_walk = n * k
print(min(time_bus, time_walk))