from collections import deque

arr = deque()
for i in range(1, int(input())+1):
    arr.append(i)
while (len(arr)>1):
    del arr[0]
    x = arr.popleft()
    arr.append(x)
    
print(arr[0])