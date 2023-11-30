L = ['A+', "A0", "B+", "B0", "C+", "C0", "D+", "D0", "", "F"]       #등급 Arr, 각 등급의 순서를 찾기 위해 사용. D0와 F의 점수차가 다른 등급과 달리 1이기 때문에 더 짧은 코드를 위해 빈 문자를 포함함.
sum_score = 0                                                       #총 학점
sum2_score = 0                                                      #학점 * 과목평점의 합
for i in range(20):
    Name, Score, Grade = input().split()
    if Grade[0] != "P" :
        sum_score += float(Score)
        sum2_score += float(Score) * (4.5 - L.index(Grade) * 0.5) 
print(round(sum2_score / sum_score, 6))                             #round() == 반올림 파이썬 내장함수, 소수점 아래 6자리까지 출력