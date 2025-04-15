def solve():
    import sys
    # Modul qiymati - odatda 1000000007, lekin masala shartiga qarab 10^7+7 ham bo‘lishi mumkin.
    mod = 1000000007  
    n = int(sys.stdin.readline().strip())
    # Tezkor hisoblash: 2^(n-1) mod mod
    result = pow(2, n - 1, mod)
    print(result)
    
# Agar input() orqali ham sinash kerak bo'lsa, quyidagicha:
if __name__ == '__main__':
    solve()