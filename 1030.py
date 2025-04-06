def find_cd(a, b, op):
    if op == '+':
        target = a + b
        for c in range(1, target):
            d = target - c
            if c != a or d != b:
                return c, d

    elif op == '-':
        target = b - a
        for c in range(1, 10**6):
            d = target + c
            if d > 10**6:
                break
            if c != a or d != b:
                return c, d

    elif op == '*':
        target = a * b
        for c in range(1, int(target**0.5) + 2):
            if target % c == 0:
                d = target // c
                if d > 10**6:
                    continue
                if c != a or d != b:
                    return c, d

    elif op == '/':
        target = b / a
        for c in range(1, 10**6):
            d = int(c * target)
            if d > 10**6:
                break
            if abs(d / c - target) < 1e-9 and (c != a or d != b):
                return c, d

    return -1, -1  # agar topilmasa


# Kirish o'qish (misol uchun)
a, b, op = input().split()
a = int(a)
b = int(b)

c, d = find_cd(a, b, op)
print(c, d)