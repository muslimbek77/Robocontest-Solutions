N= int(input())
result = [1]
j0 = 0
j1 = 1
for i in range(N):
    j2 = j1
    j1 = j1 + j0
    j0 = j2

    result.append(j1)
    

for i in result:
    print(i,end=' ')