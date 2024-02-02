from collections import deque

X, Y = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(Y)]

queue = deque()
NoneRipeCount = 0

for i in range(Y):
    for j in range(X):
        if Map[i][j] == 1:
            queue.append((i, j, 0))
        elif Map[i][j] == 0:
            NoneRipeCount += 1

days = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y, days = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= Y or ny < 0 or ny >= X or Map[nx][ny] != 0:
            continue

        Map[nx][ny] = 1
        NoneRipeCount -= 1
        queue.append((nx, ny, days + 1))

if NoneRipeCount == 0:
    print(days)
else:
    print(-1)
