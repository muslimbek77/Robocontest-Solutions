import math

# EKUB va EKOK funksiyalari
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Kiritish
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A to'plamining EKOKi
lcm_a = A[0]
for a in A[1:]:
    lcm_a = lcm(lcm_a, a)

# B to'plamining EKUBi
gcd_b = B[0]
for b in B[1:]:
    gcd_b = math.gcd(gcd_b, b)

# LCM(A) va GCD(B) oralig'ida nechta mos son borligini aniqlaymiz
count = 0
x = lcm_a
while x <= gcd_b:
    if gcd_b % x == 0:
        count += 1
    x += lcm_a

# Natijani chiqarish
print(count)