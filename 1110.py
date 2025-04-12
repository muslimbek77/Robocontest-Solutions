def beautiful_number(number):
    odd_number = 0
    even_number = 0

    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            j = number // i

            # i ni hisoblash
            if i % 2 == 0:
                even_number += 1
            else:
                odd_number += 1

            # i va j bir xil bo‘lishi mumkin (masalan 36 da i=6 bo‘lsa, j ham 6 bo‘ladi)
            if j != i:
                if j % 2 == 0:
                    even_number += 1
                else:
                    odd_number += 1

    return "YES" if odd_number == even_number else "NO"

for i in range(int(input())):
    print(beautiful_number(int(input())))
