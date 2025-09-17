l=list(map(int,list(input())))
print(sum(filter(lambda x: (x) if l[-1]%2==x%2 else 0,l )))
