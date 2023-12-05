Alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
N, B = input().split()
N = N[::-1]                                 #앞자리부터 계산하기 위한 슬라이싱
B = int(B)
Num = 0                                     #10진수 변환값
for i in range(len(N)):
    Num += Alphabet.index(N[i]) * (B ** i)  #알파벳 리스트에서의 순서로 10진수로 변환
print(Num)
