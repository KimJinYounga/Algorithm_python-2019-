import sys

q = lambda: sys.stdin.readline().strip()
N=int(q())
tree=[list(map(int, list(q()))) for i in range(N)]
visit=[[0]*N for i in range(N)]

def init(N):
    result=0
    return result

num=1
up=1
def dfs(x,y, count):
    visit[x][y]=count
    for i in range(N):
        if x+i<N and visit[x+i][y]==0 and tree[x+i][y]==1:
            dfs(x+i,y, count)
        elif x+i<N and visit[x + i][y] == 0 and tree[x + i][y] == 0:
            x-=1
            running=True
            # 좌/우 check
            while running:
                if y - num >= 0 and visit[x + i][y - num] == 0 and tree[x + i][y - num] == 1:
                    dfs(x + i, y - num, count)
                else:
                    running=False

                if y + num < N and visit[x + i][y + num] == 0 and tree[x + i][y + num] == 1:
                    dfs(x + i, y + num, count)

                else:
                    running=False
        else:
            break

        count+=1



init(N)
for i in range(N):
    for j in range(N):
        if tree[i][j]==1 and visit[i][j]==0:
            count = 0
            dfs(i, j,  count)







print("visit")
print(visit)