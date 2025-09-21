n,a,b = map(int,input().split())
d = (a**2 + b**2)**(1/2)
for i in range(n):
    if int(input())<=d:
        print("BOX")
    else:
        print("TRASH")