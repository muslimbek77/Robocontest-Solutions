def count_factors(n, m, factor):
    def count_up_to(x):
        count = 0
        while x > 0:
            x //= factor
            count += x
        return count
    return count_up_to(n) - count_up_to(m - 1)

def count_trailing_zeros(n, m):
    count_2 = count_factors(n, m, 2)
    count_5 = count_factors(n, m, 5)
    return min(count_2, count_5)

m, n = map(int,input().split())

print(count_trailing_zeros(n, m))