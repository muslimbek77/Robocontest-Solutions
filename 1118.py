import math

def prefix_sum(n):
    if n <= 0:
        return 0
    # 1) k ni topamiz:
    k = int((math.sqrt(1 + 8*n) - 1) // 2)
    if k*(k+1)//2 < n:
        k += 1
    # 2) T(k-1) va r:
    T_prev = (k-1)*k // 2
    r = n - T_prev
    # 3) S(k-1) = sum_{i=1 to k-1} i^2:
    sum_sq = (k-1)*k*(2*k-1) // 6
    # 4) P(n):
    return sum_sq + r*k

def sum_range(A, B):
    return prefix_sum(B) - prefix_sum(A-1)

# Misol:
A, B = map(int, input().split())
print(sum_range(A, B))
