j=input()
for i in j:
    if i != '9':
        j = j.replace(i,'9',1)
        break
print(j)