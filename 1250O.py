a,b,c = map(int,input().split())
if a <= c and a <= b:
  if b <= c:
    print(b,c)
  else:
    print(c,b)
elif b <= c and b <= a:
  if a <= c:
    print(a,c)
  else:
    print(c,a)
else:
  if a <= b:
    print(a,b)
  else:
    print(b,a)