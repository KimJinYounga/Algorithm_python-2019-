import sys

q = lambda: sys.stdin.readline().strip()
N,M=map(int,q().split())
tree=[list(map(int, list(q().split()))) for i in range(N)]

visit=[[0]*N for i in range(N)]
cnt=0
virus=[]
result=0

def dfs(x,y):
    global cnt
    cnt+=1
    visit[x][y] = 1
    i=1
    for i in tree[start]:
        if i not in tree:
            dfs(tree, i)

for i in range(N):
    for j in range(M):
        if tree[i][j]==2:
            virus.append([i,j])
        # dfs(i, j)
# for i in len(range(virus)):
#     dfs(virus[i][0], virus[i][1])
# print(len(virus))
for i in range(len(virus)):
    a,b=virus[i]
    dfs(a,b)
