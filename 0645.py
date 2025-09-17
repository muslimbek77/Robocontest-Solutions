a = int(input())
result = []
for i in range(int(input())):
    l,r = map(int,input().split())
    if l==r==a:
        result.append("Chiroyli")
    elif l<a or r<a:
        result.append("NO")
    else:
        result.append("Deyarli_chiroyli")
print(' '.join(result))