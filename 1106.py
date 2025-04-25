import math

def aralash_kasr(N, M):
    # M = 0 bo'lsa aniqlanmaydi
    if M == 0:
        return "INF"
    
    # Butun qism uchun floor division
    whole = N // M
    
    # Qoldiqni hosil qilamiz (doim musbat bo'ladi)
    rem = abs(N - whole * M)
    denom = abs(M)

    # Qoldiq bo'lmasa — faqat butun son
    if rem == 0:
        return str(whole)
    
    # Qoldiq/denom qismini qisqartirish
    d = math.gcd(rem, denom)
    rem //= d
    denom //= d

    # Agar butun qism 0 bo'lsa — faqat kasr
    if whole == 0:
        return f"{rem}/{denom}"
    # Aks holda — aralash shakl
    return f"{whole}+{rem}/{denom}"


if __name__ == "__main__":
    N, M = map(int, input().split())
    print(aralash_kasr(N, M))
