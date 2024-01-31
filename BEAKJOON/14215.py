A = sorted(list(map(int, input().split())))
if A[0] + A[1] <= A[2]:
    print((A[0]+A[1])*2-1)
else:
    print(sum(A))