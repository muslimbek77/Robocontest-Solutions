def reverse_number(n):
    return int(str(n)[::-1])

def find_original_number(X):
    min_candidate = None

    for abc in range(100, 1000):
        cba = reverse_number(abc)
        diff = abs(abc - cba)
        rev_diff = reverse_number(diff)

        total = diff + rev_diff

        if total == X:
            if min_candidate is None or abc < min_candidate:
                min_candidate = abc

    return min_candidate

# Foydalanuvchidan X ni olish
X = int(input())

javob = find_original_number(X)

if javob:
    print(javob)
else:
    print("Bunday son topilmadi.")
