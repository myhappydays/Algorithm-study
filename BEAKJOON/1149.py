import sys
sys.setrecursionlimit(10**6)

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
P = {}

def func(m, n, a, b, P):
    if n == len(A):
        return m
    else:
        if (n, a, b) not in P:
            P[(n, a, b)] = min(A[n][a] + func(m, n+1, b, 3-a-b, P), A[n][b] + func(m, n+1, a, 3-a-b, P))
        return P[(n, a, b)]

print(min(func(0, 0, 1, 2, P), func(0, 0, 0, 2, P), func(0, 0, 1, 2, P)))
