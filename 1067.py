import math

def find_numbers(S, P):
    D = S*S - 4*P
    if D < 0:
        return -1
    sqrt_D = int(math.isqrt(D))
    if sqrt_D * sqrt_D != D:
        return -1
    x1 = (S + sqrt_D) // 2
    x2 = (S - sqrt_D) // 2
    if x1 + x2 == S and x1 * x2 == P:
        return f"{x1} {x2}"
    return -1
S, P = map(int,input().split())
print(find_numbers(S, P))