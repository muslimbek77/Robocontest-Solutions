class Fenwick:
    def __init__(self, n):
        self.n = n
        self.f = [0] * (n+1)

    def upd(self, i, v):
        while i <= self.n:
            self.f[i] += v
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.f[i]
            i -= i & -i
        return s

    def range_query(self, l, r):
        return self.query(r) - self.query(l-1)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    # har bir qiymatning pozitsiyalarini yig'amiz
    pos = [[] for _ in range(n+1)]
    for i, x in enumerate(arr, start=1):
        pos[x].append(i)

    # juftliklarni ikkinchi pozitsiyaga qarab saralaymiz
    pairs = []
    for x in range(1, n+1):
        i, j = pos[x]
        # i < j garoviga ishonamiz
        pairs.append((j, i))
    pairs.sort()  # j bo'yicha o'sish tartibida

    # Fenwickni to'ldiramiz: boshda har bir pozitsiyada 1 ta "yashovchi" element bor
    ft = Fenwick(2*n)
    for i in range(1, 2*n+1):
        ft.upd(i, 1)

    total_ops = 0
    # har bir juftlikni eng kichik ikkinchi pozitsiya tartibida o'chiramiz
    for j, i in pairs:
        cnt_alive = ft.range_query(i, j)
        # kesishma ichidagi yashovchi elementlar soni cnt_alive,
        # ularni yonma-yon qilish uchun cnt_alive-2 ta swap va 1 ta delete:
        # jami = (cnt_alive-2) + 1 = cnt_alive-1
        total_ops += cnt_alive - 1
        # o'chirilgan elementlarni Fenwickdan olib tashlaymiz
        ft.upd(i, -1)
        ft.upd(j, -1)

    print(total_ops)


if __name__ == "__main__":
    main()
