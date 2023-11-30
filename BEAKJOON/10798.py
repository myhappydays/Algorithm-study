Input_Arr = [input() for i in range(5)]
Answer_Str = ""
for i in range(max([len(Input_Arr[l]) for l in range(5)])):
    for j in range(5):
        if len(Input_Arr[j]) > i:
            Answer_Str += Input_Arr[j][i]
print(Answer_Str)