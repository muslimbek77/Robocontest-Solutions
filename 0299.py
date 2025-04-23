# Read input from input.txt
with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

ptr = 0
# Read matrix A dimensions
N, M = map(int, lines[ptr].split())
ptr += 1

# Read matrix A
A = []
for _ in range(N):
    row = list(map(int, lines[ptr].split()))
    A.append(row)
    ptr += 1

# Read matrix B dimensions
X, Y = map(int, lines[ptr].split())
ptr += 1

# Read matrix B
B = []
for _ in range(X):
    row = list(map(int, lines[ptr].split()))
    B.append(row)
    ptr += 1

# Compute matrix multiplication
result = []
for i in range(N):
    result_row = []
    for j in range(Y):
        sum_val = 0
        for k in range(M):
            sum_val += A[i][k] * B[k][j]
        result_row.append(sum_val)
    result.append(result_row)

# Write output to output.txt
with open('output.txt', 'w') as f:
    for row in result:
        f.write(' '.join(map(str, row)) + '\n')