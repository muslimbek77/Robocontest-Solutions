result = -1
girl = 0
for i in range(int(input())):
  year,gender = map(int,input().split())
  if gender == 0:
    if girl < year:
      girl = year
      result = i + 1
print(result)