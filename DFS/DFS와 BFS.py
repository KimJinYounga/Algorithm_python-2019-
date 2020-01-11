import sys

input_s = lambda: sys.stdin.readline()

N, M, start = map(int,input_s().split())
abj = [list(map(int,input_s().split())) for i in range(M)]


tree = {}
visit_dfs = []
visit_bfs = []


def init():
   for i in range(1,N+1):
       tree[i] = []
   for i in range(M):
        tree[abj[i][0]].append(abj[i][1])
        tree[abj[i][1]].append(abj[i][0])

   for i in range(1,N+1):
        tree[i].sort()



def search_dfs(tree,start):
   visit_dfs.append(start)
   for i in tree[start]:
       if i not in visit_dfs:
           search_dfs(tree,i)


def search_bfs(tree,start):
    visit_bfs.append(start)
    qlist = []
    qlist.append(start)
    while qlist:
        node=qlist.pop(0)
        for i in tree[node]:
            if i not in visit_bfs:
                visit_bfs.append(i)
                if i not in qlist:
                    qlist.append(i)


def show(list):
   for i in list:
       print(i,end=' ')
   print()

init()
print(tree)
search_dfs(tree, start)
search_bfs(tree,start)
show(visit_dfs)
show(visit_bfs)