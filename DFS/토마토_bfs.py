import sys
from collections import deque

q=lambda: sys.stdin.readline().strip()
M,N=map(int, q().split())
tree=[list(map(int, q().split())) for i in range(N)]
result=-1

# 1인 부분 리스트에 저장하고 bfs를 동시에 시작하기
# 1인 부분의 상하좌우에 해당하는 갯수만큼 for loop로 돌리기
# while문을 다 돌았는데 0이 아직 있다면 0을 출력 외엔 count출력

def bfs(start):
    global result
    qlist=deque(start)
    while qlist:
        for i in range(len(qlist)):
            node=qlist.popleft()
            # 상하좌우 1인지 0인지 검사
            # 0일 경우에 1로 바꾸기
            # -1일 경우 바꾸지 않기, 추가조건있어야할듯 ==> -1인경우 qlist에 넣지않기면 될듯
            # M=6 N=4

            # 아래 검사
            if node[0] + 1 < N:
                if tree[node[0] + 1][node[1]] == 0:
                    tree[node[0] + 1][node[1]] = True
                    qlist.append([node[0] + 1, node[1]])

            # 위 검사
            if node[0] - 1 >= 0:
                if tree[node[0] - 1][node[1]] == 0:
                    tree[node[0] - 1][node[1]] = True
                    qlist.append([node[0] - 1, node[1]])

            # 오른쪽 검사
            if node[1] + 1 < M:
                if tree[node[0]][node[1] + 1] == 0:
                    tree[node[0]][node[1] + 1] = True
                    qlist.append([node[0], node[1] + 1])

            # 왼쪽 검사
            if node[1] - 1 >= 0:
                if tree[node[0]][node[1] - 1] == 0:
                    tree[node[0]][node[1] - 1] = True
                    qlist.append([node[0], node[1] - 1])

        result+=1
    for i in tree:
        if 0 in i:
            result=-1
    return result

ripe=[]
# M=6, N=4
for i in range(N):
    for j in range(M):
        if tree[i][j]==1:
            ripe.append([i,j])

bfs(ripe)
print(result)