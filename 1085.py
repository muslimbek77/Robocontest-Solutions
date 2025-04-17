def ascii_deshifrlash(shifrlangan: str) -> str:
    i = 0
    natija = ''
    while i < len(shifrlangan):
        # Dastlab 3 ta raqamni olib ko'ramiz
        uch_xona = int(shifrlangan[i:i+3])
        if 65 <= uch_xona <= 122:
            natija += chr(uch_xona)
            i += 3
        else:
            ikki_xona = int(shifrlangan[i:i+2])
            natija += chr(ikki_xona)
            i += 2
    return natija

# Misol uchun
shifrlangan_matn = input()
print(ascii_deshifrlash(shifrlangan_matn))  # Natija: Salom