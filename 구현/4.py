'''  >> 게임 개발 <<  '''

# N값, M값 입력
n, m = map(int, input().split())

# *****key*****
# 방문한 곳 저장해야 함
d = [[0] * m for _ in range(n)]

# 현재 위치 입력
a, b, dir = map(int, input().split()) # (A, B) direction 입력
d[a][b] = 1 # 현재 좌표를 방문한 곳으로 처리함(1)

# 맵 정보 입력
array=[]
for i in range(n):
    array.append(list(map(int, input().split())))

# *****key*****
# 북동남서 방향 정의
dx = [-1, 0, 1, 0] # dx는 아래로 한칸이니까
dy = [0, 1, 0, -1] # dy는 오른쪽으로 한칸이니까