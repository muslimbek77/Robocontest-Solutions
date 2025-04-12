import math

def ekub1(a, b, c, d):
    # 1. a^b mod d ni hisoblaymiz
    mod_exp = pow(a, b, d)
    # 2. c ning d bo‘yicha qoldig‘i
    c_mod = c % d
    # 3. (a^b - c) mod d ni hisoblaymiz, bu yerda mod noqulay holatlarni oldini olish uchun d ni qo‘shamiz
    X = (mod_exp - c_mod + d) % d
    # 4. EKUB ni hisoblash
    return math.gcd(X, d)

a, b, c, d = map(int, input().split())
print(ekub1(a, b, c, d))
