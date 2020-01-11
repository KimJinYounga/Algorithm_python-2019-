import sys

input_s = lambda: sys.stdin.readline()

N, M, start = map(int,input_s().split())
abj = [list(map(int,input_s().split())) for i in range(M)]
# 뒤에 정렬 후 앞 정렬 -> 최종적으론 x[0]으로 오름차순 정렬 (같으면 뒤 기준 오름차순)
abj.sort(key=lambda x: x[1])
abj.sort(key=lambda x: x[0])

tree = {}
visit_dfs = []

visit_bfs = []
queue_bfs = []

def init():
   for i in range(1,N+1):
       tree[i] = []
   for i in range(M):
       if abj[i][1] not in tree[abj[i][0]]:
           tree[abj[i][0]].append(abj[i][1])
       if abj[i][0] not in tree[abj[i][1]]:
           tree[abj[i][1]].append(abj[i][0])

# 재귀 형식으로 visit_dfs에 방문한 노드 stack을 사용하여 출력

init()
print(tree)