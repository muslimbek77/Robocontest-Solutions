N,A,D = map(int,input().split())
result = []
j = A
for i in range(N):
    result.append(j)
    j *= D

for i in result:
    print(i,end=' ')