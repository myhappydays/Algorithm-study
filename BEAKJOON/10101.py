A = sorted([int(input()) for _ in range(3)])
if sum(A) != 180:
    print("Error")
elif A[0] == A[1] and A[1] == A[2]:
    print("Equilateral")
elif A[0] == A[1] or A[1] == A[2]:
    print("Isosceles")
else:
    print("Scalene")