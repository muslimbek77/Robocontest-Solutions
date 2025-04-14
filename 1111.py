def umumiy_boluvchilar_soni(n, m):
    # Eng kichikini topamiz
    kichik = min(n, m)
    # Hisoblagich
    count = 0
    # 1 dan kichik songacha bo'lgan barcha sonlarni tekshiramiz
    for i in range(1, kichik + 1):
        if n % i == 0 and m % i == 0:
            count += 1
    return count
a, b = map(int, input().split())
print(umumiy_boluvchilar_soni(a, b))