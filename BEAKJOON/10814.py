# 입력 받기
N = int(input())
members = [(int(age), name) for _ in range(N) for age, name in [input().split()]]

members.sort(key=lambda x: (x[0]))

for member in members:
    print(member[0], member[1])
