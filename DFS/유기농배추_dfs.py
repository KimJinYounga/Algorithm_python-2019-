import sys
sys.setrecursionlimit(10000)
q = lambda: sys.stdin.readline().strip()
num=int(q())

def dfs(x,y):
    global cnt
    cnt+=1
    visit[x][y] = 1
    i=1
    if x + i < N and tree[x + i][y] == 1 and visit[x + i][y] == 0:
        dfs(x + i, y)
    if x - i >= 0 and tree[x - i][y] == 1 and visit[x - i][y] == 0:
        dfs(x - i, y)
    if y + i < M and tree[x][y + i] == 1 and visit[x][y + i] == 0:
        dfs(x, y + i)
    if y - i >= 0 and tree[x][y - i] == 1 and visit[x][y - i] == 0:
        dfs(x, y - i)

ans=[]
for n in range(num):
    apt=[]
    M, N, K = map(int, q().split())
    tree = [[0] * M for i in range(N)]
    visit = [[0] * M for i in range(N)]
    for i in range(K):
        b, a = map(int, q().split())
        tree[a][b] = 1
    for i in range(N):
        for j in range(M):
            if tree[i][j] == 1 and visit[i][j] == 0:
                cnt = 0
                dfs(i, j)
                apt.append(cnt)
    ans.append(len(apt))

for i in ans:
    print(i)