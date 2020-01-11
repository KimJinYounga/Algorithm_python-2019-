# import sys
#
# input_s = lambda: sys.stdin.readline()
#
# M = int(input_s())
# abj = [list(map(int,input_s().split())) for i in range(M)]
#
# abj.sort(key=lambda x: x[1])
# abj.sort(key=lambda x: x[0])
#
# for i in range(M):
#     print(abj[i][0],abj[i][1])
N = int(input())

point = []

for i in range(N):
    p = input().split()
    p[0] = int(p[0])
    p[1] = int(p[1])

    point.append(p)

point.sort()

for j in point:
    print(j[0], j[1])