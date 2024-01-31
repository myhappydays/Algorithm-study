A = int(input())
Log = [-1 for _ in range(A)]

def func(N):
    if N < 3:
        return(N)%10007
    else:
        if Log[N-1] == -1:
            F = func(N-1) + func(N-2)
            Log[N-1] = F
            return F%10007
        else:
            return(Log[N-1])%10007

print(func(A))
