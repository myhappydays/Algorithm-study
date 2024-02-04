while True:
    A = sorted(list(map(int, input().split())))
    if sum(A) == 0: break
    print("right" if A[0]**2 + A[1]**2 == A[2]**2 else "wrong")
    