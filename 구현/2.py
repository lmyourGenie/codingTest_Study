# 시각(Time)
n = int(input()) # N값 입력

count = 0

for i in range(n + 1):
    for j in range(60): #분
        for k in range(60): #초
            # 매 시각 안에 '3'이 포함되어 있으면 카운트 증가
            # 나열해서 확인
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)