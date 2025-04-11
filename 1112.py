def ozini_boluvchi_son(son):
    if '0' in  str(son):
        return False
    for i in str(son):
        if son % int(i) != 0:
            return False
    return True

L, R = map(int, input().split())
result = 0
for i in range(L,R+1):
  result += ozini_boluvchi_son(i)

print(result)
    