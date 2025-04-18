import math

def find_numbers(a, b):
    D = a * a - 4 * b  # Diskriminant
    if D < 0:
        return []  # Haqiqiy ildizlar mavjud emas

    sqrt_D = math.isqrt(D)
    if sqrt_D * sqrt_D != D:
        return []  # Diskriminant kvadrat ildizi butun emas

    x1 = (a + sqrt_D) // 2
    x2 = (a - sqrt_D) // 2

    # Tekshirish: x1 va x2 butun sonlar bo‘lishi kerak
    if x1 + x2 != a or x1 * x2 != b:
        return []

    # Ikkala tartibda ham yechimlar mavjud bo‘lishi mumkin
    if x1 == x2:
        return [[x1, x2]]
    else:
        return [[x1, x2], [x2, x1]]

# Kirish ma'lumotlarini o'qish
a, b = map(int, input().split())

# Natijani topish
results = find_numbers(a, b)

# Natijani chiqarish
if not results:
    print(-1)
else:
    for pair in results:
        print(f"{pair[0]} {pair[1]}")
