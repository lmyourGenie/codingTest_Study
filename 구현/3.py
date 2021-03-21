# 왕실의 나이트
input_data = input() # 시작 위치 입력

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
# ord : 문자의 아스키 코드 값을 돌려주는 함수

# 일단 나이트가 이동할 수 있는 8가지 방법을 정리하자
steps = [(-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2)]

# 시작 위치에 따라 각 위치로 이동이 가능한지 확인
result = 0 # 가능하면 카운트할 것
for step in steps:
    # 입력했던 row column에다가  8가지의 +-계산을 해본다.
    next_row = row + step[0]
    next_column = column + step[1]
    # 이동이 가능하면(즉, 숫자가 좌표 평면상에 위치하면) 카운트 증가
    if next_row >= 1 and next_column <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)