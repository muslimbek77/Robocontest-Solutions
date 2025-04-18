def parse_c_integer_literal(s):
    s = s.strip()
    negative = False

    # Manfiy sonni aniqlash
    if s.startswith('-'):
        negative = True
        s = s[1:]

    # Sonning asosini aniqlash
    if s.startswith(('0x', '0X')):
        base = 16
        s = s[2:]
    elif s.startswith('0') and len(s) > 1:
        base = 8
        s = s[1:]
    else:
        base = 10

    # Sonni kerakli asosda butun songa o‘tkazish
    value = int(s, base)

    # Agar manfiy bo‘lsa, qiymatni manfiylashtirish
    if negative:
        value = -value

    return value
print(parse_c_integer_literal(input()))
