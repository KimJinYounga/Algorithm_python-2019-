# import sys
#
# q = lambda: sys.stdin.readline().strip()
# N=int(q())
# tree=[list(map(int, list(q()))) for i in range(N)]
# visit=[[0]*N for i in range(N)]
#
# def init(N):
#     result=0
#     print(tree)
#     return result
#
# def dfs(tree, x, y, count):
#
#     for i in range(1,N):
#         if 0 <= x + i< N:
#             if visit[x + i][y] == 0 and tree[x + i][y] == 1:
#                 visit[x + i][y] = count
#                 dfs(tree, x + i, y, count)
#                 print("visit")
#                 print(visit)
#             elif visit[x + i][y] == 0 and tree[x + i][y] == 0:
#                 x-=1
#
#                 for j in range(N):
#                     if 0 <= y + j < N:
#                         if visit[x + i][y + j] == 0 and tree[x + i][y + j] == 1:
#                             visit[x + i][y + j] = count
#                             dfs(tree, x + i, y + j, count)
#                         else:
#                             break
#
#                     if 0 <= y - j < N:
#                         if visit[x + i][y - j] == 0 and tree[x + i-1][y - j] == 1:
#                             visit[x + i][y - j] = count
#                             dfs(tree, x + i, y - j, count)
#                         else:
#                             break
#                 print("visit")
#                 print(visit)
#
#
# init(N)
# count=0
# for i in range(N):
#     for j in range(N):
#         if tree[i][j]==1 and visit[i][j]==0:
#             dfs(tree, i, j,  count)
#
#
#
# print("visit")
# print(visit)
import sys
read = lambda : sys.stdin.readline().strip()

n = int(read())

def dfs(matrix, cnt, x,y):
    matrix[x][y]=0
    # 이건 이제 이미 간것이다. 하고 0으로 바꾸는것 이다.
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]
        # 이 근처 다 n_x, n_y로 간다.
        if n_x>=0 and n_x<n and n_y>=0 and n_y<n:
            # 범위 check
            if matrix[n_x][n_y]==1:
            # 그부분이 1이면
                cnt = dfs(matrix, cnt+1, n_x, n_y)
                # cnt를 증가시켜서 다시한번 그 근처 확인
    return cnt
    # 다 cnt검사하면 끝을 낸다.

matrix = [list(map(int, list(read()))) for _ in range(n)]
# matrix에 input값 넣기

ans = []
for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            # 일단 1로 뭔가의 그룹이다.
            ans.append(dfs(matrix, 1, i, j))

print(len(ans))
for i in sorted(ans):
    print(i)