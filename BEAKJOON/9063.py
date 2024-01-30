I = int(input())
A = [list(map(int, input().split())) for _ in range(I)]
X = max([A[i][0] for i in range(I)]) - min([A[i][0] for i in range(I)])
Y = max([A[i][1] for i in range(I)]) - min([A[i][1] for i in range(I)])
print(X*Y)