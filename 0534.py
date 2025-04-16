# Modul qiymati
M = 10**9 + 7

# Kirish: n sonini o'qiymiz.
n = int(input())

# n, n+1, n+2, n+3 ning M ga nisbatan qismlarini hisoblaymiz
n_mod   = n % M
n1_mod  = (n + 1) % M
n2_mod  = (n + 2) % M
n3_mod  = (n + 3) % M

# Hosil: (n*(n+1)*(n+2)*(n+3)) % M
product = (n_mod * n1_mod % M) * (n2_mod * n3_mod % M) % M

# 24 ga modul M bo'yicha teskari elementini topamiz
inv24 = pow(24, M-2, M)

# Natijani hisoblaymiz
result = product * inv24 % M

print(result)
