import sys
q=lambda: sys.stdin.readline().strip()
N,M=map(int, q().split())
tree=[list(map(int, list(q()))) for i in range(N)]
visit=[[False]*M for i in range(N)]
count=0
def bfs(x,y):
    global count
    qlist = []
    visit[0][0]=True
    qlist.append([x,y])
    count=1
    while qlist:
        if visit[N - 1][M - 1] == 1:
            return 0
        for i in range(len(qlist)):
            node = qlist.pop(0)
            # 아래 검사
            if node[0] + 1 < N:
                if tree[node[0] + 1][node[1]] == 1 and visit[node[0] + 1][node[1]] == False:
                    visit[node[0] + 1][node[1]] = True
                    qlist.append([node[0] + 1, node[1]])

            # 위 검사
            if node[0] - 1 >= 0:
                if tree[node[0] - 1][node[1]] == 1 and visit[node[0] - 1][node[1]] == False:
                    visit[node[0] - 1][node[1]] = True
                    qlist.append([node[0] - 1, node[1]])

            # 오른쪽 검사
            if node[1] + 1 < M:
                if tree[node[0]][node[1] + 1] == 1 and visit[node[0]][node[1] + 1] == False:
                    visit[node[0]][node[1] + 1] = True
                    qlist.append([node[0], node[1] + 1])

            # 왼쪽 검사
            if node[1] - 1 >= 0:
                if tree[node[0]][node[1] - 1] == 1 and visit[node[0]][node[1] - 1] == False:
                    visit[node[0]][node[1] - 1] = True
                    qlist.append([node[0], node[1] - 1])

        count += 1

bfs(0,0)
print(count)