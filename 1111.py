import math

def umumiy_boluvchilar_soni(n, m):
    # n va m ning eng katta umumiy bo'luvchisini topamiz
    g = math.gcd(n, m)
    count = 0
    # g ning ildizigacha bo'lgan sonlarni tekshiramiz
    for i in range(1, int(math.sqrt(g)) + 1):
        if g % i == 0:
            # Agar i ning kvadrati g ga teng bo'lsa, ikkita o'rniga bitta bo'luvchi hisoblanadi
            if i * i == g:
                count += 1
            else:
                count += 2  # i va g//i ikki xil bo'luvchi
    return count

# Input olib, natijani chiqaramiz
a, b = map(int, input().split())
print(umumiy_boluvchilar_soni(a, b))