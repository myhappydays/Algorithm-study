List = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = map(int, input().split())
answer = ""

while N != 0:
    answer = List[N%B]+answer
    N //= B

print(answer)