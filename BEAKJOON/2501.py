N, K = map(int, input().split())
I = 0

for i in range(1, N+1):
    if N % i == 0:
        I += 1
    if I == K:
        print(i)
        break
    if i == N:
        print(0)
    