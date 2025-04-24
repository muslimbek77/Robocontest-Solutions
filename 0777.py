n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == 0:
    print(0)
else:
    divisors = set()
    for i in range(1, int(k**0.5) + 1):
        if k % i == 0:
            divisors.add(i)
            divisors.add(k // i)
    a_set = set(a)
    count = 0
    for d in divisors:
        if d not in a_set:
            count += 1
    print(count)