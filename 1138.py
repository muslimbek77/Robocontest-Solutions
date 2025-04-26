import math

def check_solution(a, b, c):
    gcd_ab = math.gcd(a, b)
    
    if c % gcd_ab == 0:
        return "Yes"
    else:
        return "No"
for _ in range(int(input())):
  a, b, c = map(int,input().split())
  print(check_solution(a, b, c))