N=int(input())
A=[int(input()) for i in range(N)]

def solution(N,A):
    A=sorted(A)
    list=[]
    for i in range(N):
        list.append(A[i]*N)
        N-=1
    result=max(list)
    return result

print(solution(N,A))


#
# 7
#
# 1 = 7
# 2 = 12
# 3 = 15
# 6 = 24
# 7 = 21
# 8 = 16
# 10 = 10
#
#
# 2
#
# 10 = 20
# 15 = 15