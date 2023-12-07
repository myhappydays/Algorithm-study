N = int(input())
dots = 2

for i in range(N):
    dots += dots - 1

print(dots**2)