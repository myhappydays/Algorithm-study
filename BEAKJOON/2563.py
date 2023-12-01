I = int(input())                            #색종이의 수
Paper_Arr = [[0, 0] for i in range(I)]      #색종이의 위치 *2차원 정수 배열
for i in range(I):
    Paper_Arr[i][0], Paper_Arr[i][1] = map(int, input().split())
Black = 100 * I
Black2 = 0

for a, i in enumerate(Paper_Arr):
    for b, j in enumerate(Paper_Arr):
        if j[0] <= i[0] and i[0] >= j[0] + 10:
            Black2 += (10 - abs(i[0] - j[0])) * (10 - abs(i[1] - j[1]))

Black -= int(Black2 / 2)
print(Black)