def top_yoqolgan_son(sonlar):
    sonlar.sort()
    a, b, c = sonlar

    # Har bir ehtimoliy yo'qolgan joyni ko'rib chiqamiz
    # 1. (x, a, b, c)
    d1 = b - a
    if a - d1 == 2 * d1 - (c - b):  # Progressiya to'g'ri bo'lishi uchun
        return a - d1
    
    # 2. (a, x, b, c)
    if (b - a) == (c - b) * 2:
        return (a + b) // 2

    # 3. (a, b, x, c)
    if (b - a) * 2 == (c - b):
        return (b + c) // 2

    # 4. (a, b, c, x)
    d2 = c - b
    if d2 == b - a:
        return c + d2

    return "Yechim topilmadi"

# Kirish
sonlar = list(map(int, input().split()))

# Chiqish
print(top_yoqolgan_son(sonlar))