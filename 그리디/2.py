#1이 될 때까지
import sys

n, k = map(int, input().split())
result = 0

# 입력 조건
if n not in range(2, 100000) or k not in range(2, 100000):
    print("Please enter a valid input")
    sys.exit() # 종료

while True:
    # N이 K로 나누어지지 않을 때는
    # 나누어지는 수가 될 때까지 1을 뺀다. (방법1)
    target = (n // k) * k
    result += n - target
    n = target

    # 더이상 나눌 수 없을 때 반복문 탈출
    if n < k:
        break

    # K로 나누기 (방법2)
    result += 1
    n //= k


# 계속 나누다보면 끝엔 결국 1이 남으므로 뺀다.
result += n - 1
print(result)