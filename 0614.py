V,Azim,Aziz,Akbar = map(int, input().split())

while True:
    V = V - Azim
    if V < 0:
        print("Azim")
        break
    V = V - Aziz
    if V < 0:
        print("Aziz")
        break
    V = V - Akbar
    if V < 0:
        print("Akbar")
        break