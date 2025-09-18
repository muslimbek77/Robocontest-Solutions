def add_welcome(func):
    def wrapper(x, y):
        # Yuqori qatorlar
        for i in range(x // 2):
            func(i, y)

        # O'rtadagi qator
        print("WELCOME".center(y, "-"))

        # Pastki qatorlar (simmetrik)
        for i in range(x // 2 - 1, -1, -1):
            func(i, y)
    return wrapper


@add_welcome
def draw_pattern(i, y):
    # To'g'ri naqsh: "*|*" (2*i+1) marta takrorlanadi
    pattern = "*|*" * (2 * i + 1)
    print(pattern.center(y, "-"))



x, y = map(int, input().split())
draw_pattern(x, y)