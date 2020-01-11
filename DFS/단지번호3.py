import sys

q = lambda: sys.stdin.readline().strip()
N=int(q())
tree=[list(map(int, list(q()))) for i in range(N)]
visit=[[0]*N for i in range(N)]
cnt=0
apt=[]
result=0

def dfs(x,y):
    global cnt
    cnt+=1
    visit[x][y] = 1
    i=1
    if x + i < N and tree[x + i][y] == 1 and visit[x + i][y] == 0:
        dfs(x + i, y)
    if x - i >= 0 and tree[x - i][y] == 1 and visit[x - i][y] == 0:
        dfs(x - i, y)
    if y + i < N and tree[x][y + i] == 1 and visit[x][y + i] == 0:
        dfs(x, y + i)
    if y - i >= 0 and tree[x][y - i] == 1 and visit[x][y - i] == 0:
        dfs(x, y - i)

for i in range(N):
    for j in range(N):
        if tree[i][j]==1 and visit[i][j]==0:
            cnt = 0
            dfs(i,j)
            apt.append(cnt)




print(len(apt))
apt.sort()
for i in apt:
    print(i)



