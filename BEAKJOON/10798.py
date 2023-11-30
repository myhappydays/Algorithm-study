Input_Arr = [input() for i in range(5)]                     #STR 1차원 배열
Answer_Str = ""
for i in range(max([len(Input_Arr[l]) for l in range(5)])): #Input_Arr의 최장 STR
    for j in range(5):
        if len(Input_Arr[j]) > i:
            Answer_Str += Input_Arr[j][i]                   #행, 열 반대
print(Answer_Str)