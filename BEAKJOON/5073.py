while True:
    A = sorted(list(map(int, input().split())))
    if sum(A) == 0:
        break
    elif A[0] + A[1] <= A[2]:
        print("Invalid")
    elif A[0] == A[1] and A[1] == A[2]:
        print("Equilateral")
    elif A[0] == A[1] or A[1] == A[2]:
        print("Isosceles")
    else:
        print("Scalene")