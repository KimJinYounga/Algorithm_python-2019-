N,K = list(map(int, input().split()))
A=[int(input()) for i in range(N)]
A.sort(reverse=True)

def solution(N,K,A):
    result=0
    for i in range(N):
        result+=int(K/A[i])
        K %= A[i]
    return result

print(solution(N,K,A))