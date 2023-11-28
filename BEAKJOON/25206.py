L = ['A+', "A0", "B+", "B0", "C+", "C0", "D+", "D0", "", "F"]
sum_score = 0
sum2_score = 0
for i in range(20):
    Name, Score, Grade = input().split()
    if Grade[0] != "P" :
        sum_score += float(Score)
        sum2_score += float(Score) * (4.5 - L.index(Grade) * 0.5) 
print(round(sum2_score / sum_score, 6))