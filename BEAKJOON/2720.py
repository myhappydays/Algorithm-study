for i in range(int(input())):
    N = int(input())
    A = [0, 0, 0, 0]
    
    A[0] = N // 25
    N %= 25
    A[1] = N // 10
    N %= 10
    A[2] = N // 5
    N %= 5
    A[3] = N // 1

    print(*A, sep=' ')
    