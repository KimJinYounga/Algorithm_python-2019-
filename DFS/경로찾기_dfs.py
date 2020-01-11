import sys
q = lambda: sys.stdin.readline()
N=int(q())

tree=[list(map(int,q().split())) for i in range(N)]
# 2차원 배열 visit를 False로 전부 초기화
visit=[[False]*N for i in range(N)]
print(visit)
print(tree)

def dfs(x,y):
    tree[x][y]=1
    visit[x][y]=True
    for i in range(N):
        # visit[x][i]==False여야 dfs함수의 for loop가 끝나며 main문의 i가 증가함
        if visit[x][i]==False and tree[y][i]==1:
            dfs(x,i)


for i in range(N):
    for j in range(N):
        if tree[i][j]==1 and visit[i][j]==False:
            dfs(i,j)

for i in range(N):
    for j in range(N):
        print(tree[i][j], end=' ')
    print()