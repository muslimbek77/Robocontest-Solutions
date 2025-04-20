def pow_3(exponent):
    result = 1
    for _ in range(exponent):
        result *= 3
    return result

def compute_S(m):
    if m < 0:
        return 0
    if m == 0:
        return 1

    b = 0
    while (1 << (b + 1)) <= m:
        b += 1

    rem = m - (1 << b)
    return pow_3(b) + 2 * compute_S(rem)

def main():
    N = int(input())
    total = N * (N + 3) // 2
    sum_odds = compute_S(N) - 1
    answer = total - sum_odds
    print(answer)

if __name__ == "__main__":
    main()