import sys

input_s = lambda: sys.stdin.readline()

N, M= map(int,input_s().split())
abj = [list(map(int,input_s().split())) for i in range(M)]
abj.sort(key=lambda x: x[1])
abj.sort(key=lambda x: x[0])

tree = {}
visit_dfs = []
def init():
   for i in range(1,N+1):
       tree[i] = []
   for i in range(M):
       if abj[i][1] not in tree[abj[i][0]]:
           tree[abj[i][0]].append(abj[i][1])
       if abj[i][0] not in tree[abj[i][1]]:
           tree[abj[i][1]].append(abj[i][0])



def search_dfs(tree,start):
   visit_dfs.append(start)
   for i in tree[start]:
       if i not in visit_dfs:
           search_dfs(tree,i)


init()
running=True
count=0
start=1
lists=[i+1 for i in range(N)]

while running:
    search_dfs(tree, start)
    count+=1
    s=list(set(lists)-set(visit_dfs))
    if len(s)==0:
        running=False
    else:
        start=s[0]
print(count)