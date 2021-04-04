'''  >> 게임 개발 <<  '''

# N값, M값 입력
n, m = map(int, input().split())

# *****key*****
# 방문한 곳 저장해야 함
d = [[0] * m for _ in range(n)]

# 현재 위치 입력
x, y, dir = map(int, input().split()) # (A, B) direction 입력
d[x][y] = 1 # 현재 좌표를 방문한 곳으로 처리함(1)

# 맵 정보 입력
array=[]
for i in range(n):
    array.append(list(map(int, input().split())))

# *****key*****
# 북동남서 방향 정의
dx = [-1, 0, 1, 0] # dx는 아래로 한칸이니까
dy = [0, 1, 0, -1] # dy는 오른쪽으로 한칸이니까

# 왼쪽(반시계 방향)으로 회전
def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]

    # 가보지 않은 칸이 존재하면 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1 # 방문한 곳으로 처리 (1)
        x = nx
        y = ny
        count += 1 # 새로운 곳에 랜드마크 찍었으니까 count +1
        turn_time = 0
        continue

    # 주변이 다 가본 곳이거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수가 없음
    if turn_time == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        # 뒤로 갈 수 있으면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막히면 끝!
        else:
            break
        turn_time = 0

print(count)