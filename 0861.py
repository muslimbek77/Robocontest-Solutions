# Baraban (bo'shliqsiz variant)
prizes = ["15SMS","2Beep","30MB","Qayta_urinish","100Daq","15Daq","30SMS",
          "100SMS","50MB","1Beep","50Daq","3Beep","50SMS","100MB","15MB","4Beep","30Daq"]

# Chiqish uchun chiroyli format (bo'shliqli variant)
pretty = ["15 SMS","2 Beep","30 MB","Qayta_urinish","100 Daq","15 Daq","30 SMS",
          "100 SMS","50 MB","1 Beep","50 Daq","3 Beep","50 SMS","100 MB","15 MB","4 Beep","30 Daq"]

# Kirish
s = input().strip()
N, K = map(int, input().split())

# Boshlang'ich indeks
index = prizes.index(s)

# Yakuniy indeks
final_index = (index + N * K) % len(prizes)

# Natija
result = prizes[final_index]

print(pretty[prizes.index(result)])