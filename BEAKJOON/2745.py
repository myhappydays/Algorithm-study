Alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'Y', 'X', 'Y', 'Z']
N, B = input().split()
N = N[::-1]
B = int(B)
Num = 0
for i in range(len(N)):
    Num += Alphabet.index(N[i]) * (B ** i)
print(Num)
