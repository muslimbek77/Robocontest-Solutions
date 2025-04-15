def solve():
    import sys
    # Input'ni o'qib olamiz. (Fayl yoki onlayn sudlovchi uchun)
    data = sys.stdin.read().strip()
    if not data:
        return
    N = int(data)
    
    # Agar N 2 ning darajasi bo'lsa, unda bosqichlar soni = log₂(N)
    # Python dagi bit_length() funksiyasi: masalan, 8 ning bit_length() = 4, 4-1 = 3 bosqich.
    rounds = N.bit_length() - 1
    print(rounds)
    
if __name__ == '__main__':
    solve()