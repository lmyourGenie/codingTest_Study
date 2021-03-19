#큰 수의 법칙
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

# 가장 큰 수
top1 = data[n-1]
# 두 번째로 큰 수
top2 = data[n-2]

result = 0

while True:
    # 첫 번째 입력조건
    # n, m, k의 범위에 맞지 않는 수면 반복문 탈출
    if n not in range(2, 1000) or m not in range(1, 10000) or k not in range(1, 10000):
        print("Please enter a valid input")
        break

    # 두 번째 입력조건
    # K는 항상 M보다 작거나 같아야 함
    if k > m:
        print("Please enter a valid input")
        break

    for i in range(k): # 가장 큰 수 k번 더하기
        if m == 0 : # m이 줄어들다가 0이 되면 반복문 탈출
            break

        result += top1 # 가장 큰 수를 한 번 더하기
        m -= 1

    if m == 0: # m이 0이면 반복문 탈출
        break
    result += top2 # 두 번째로 큰 수를 한 번 더하기
    m -= 1

print(result)
