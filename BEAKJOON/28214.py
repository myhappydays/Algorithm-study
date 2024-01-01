N, K, P = map(int, input().split())
B = list(map(int, input().split()))
available = 0

for i in range(N):
    b = B[i*K:i*K+K]
    if K - sum(b) < P:
        available += 1

print(available)