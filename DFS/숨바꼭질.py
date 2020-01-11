import sys
q=lambda: sys.stdin.readline().strip()
N,M=map(int, q().split())
visit=[False]*100001
count=0

def bfs(x):
    global count
    qlist = []
    if N==M:
        return 0

    count = 1
    visit[x]=True
    qlist.append(x)
    cal=[-1,1]
    while qlist:
        for i in range(len(qlist)):
            node = qlist.pop(0)
            for k in range(3):

                if k==2:
                    num=node*2
                else:
                    num=node+cal[k]
                if M == num:
                    return count

                if 0 <= num and num <=100000 and visit[num]==False:
                    visit[num]=True
                    qlist.append(num)
        count += 1

    return count

print(bfs(N))