N, B = input().split()
N = N[::-1]                                             #앞자리부터 계산하기 위한 슬라이싱
B = int(B)
Num = 0                                                 #10진수 변환값
for i in range(len(N)):
    ascii = ord(N[i])                                   #ord == string to askii
    decimal = ascii-48 if ascii < 65 else ascii-55      #ascii 코드의 문자 '0' == 48, 문자 'A' == '65'이기에 각각 0, 10으로 만들었음.
    Num += decimal * (B ** i)
print(Num)
