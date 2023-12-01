I = int(input())                            #색종이의 수
Paper_Arr = [[0, 0] for i in range(I)]      #색종이의 위치 *2차원 정수 배열
for i in range(I):
    Paper_Arr[i][0], Paper_Arr[i][1] = map(int, input().split())
Black = 0

for i in range(max([Paper_Arr[a][0] for a in range(I)]) + 10):     #색종이의 세로 정점
    for j in range(max([Paper_Arr[b][0] for b in range(I)]) + 10):     #색종이의 가로 정점
        for k in range(I):
            if Paper_Arr[k][0] <= i >= Paper_Arr[k][0] + 10 and Paper_Arr[k][1] <= j >= Paper_Arr[k][1] + 10:
                Black += 1
                break

print(Black)