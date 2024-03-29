import sys
input = sys.stdin.readline

n,m = map(int,input().split())
matrix = []
visit = [[0] * m for _ in range(n)]
x, y, d = map(int,input().split())

# d => 0,3,2,1 순서로 돌아야한다.
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(n):
    matrix.append(list(map(int,input().split())))

# 처음 시작하는 곳 방문 처리
visit[x][y] = 1
count = 1

while True:
    flag = False
    # 4방향 확인
    for _ in range(4):
        # 한번 돌았으면 그 방향으로 작업시작
        d = (d+3)%4
        
        # 현재 방향에서 반시계 방향 90도 회줜
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
            if not visit[nx][ny]:
                visit[nx][ny] = 1
                count += 1
                x, y = nx, ny
                #청소 한 방향이라도 했으면 다음으로 넘어감
                flag = True
                break
    if not flag: # 4방향 모두 청소가 되어 있을 때,
        nx, ny = x - dx[d], y - dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 1: #후진했는데 벽
                print(count)
                break
            else:
                x, y = nx, ny
