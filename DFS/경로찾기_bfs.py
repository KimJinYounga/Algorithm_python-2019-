import sys
q = lambda: sys.stdin.readline()
N=int(q())

tree=[list(map(int,q().split())) for i in range(N)]
# 2차원 배열 visit를 False로 전부 초기화

def bfs(x):
    visit = [False for i in range(N)]
    qlist = []
    qlist.append(x)
    while qlist:
        node=qlist.pop(0)
        print("node")
        print(node)
        for i in range(N):
            if tree[node][i]==1 and visit[i]==False:
                visit[i]=True
                tree[x][i]=1
                print("Tree")
                print(tree)
                qlist.append(i)
                print("i")
                print(i)
                print("qlist")
                print(qlist)
    print(tree)

for i in range(N):
    bfs(i)

for i in range(N):
    for j in range(N):
        print(tree[i][j], end=' ')
    print()