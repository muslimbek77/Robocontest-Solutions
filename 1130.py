def max_fill(M, A, B):
    max_suv = 0
    # a ni 0 dan M//A gacha aylanamiz
    for a in range(M // A + 1):
        # Qolgan hajmga mos keladigan maksimal b ni hisoblaymiz
        b = (M - a * A) // B
        total = a * A + b * B
        if total > max_suv:
            max_suv = total
    return max_suv


A, B, M = map(int, input().split())
print(max_fill(M, A, B))  
