N,M,K=list(map(int, input().split()))

def solution(N,M,K):
    for i in range(K):
        if N > M * 2:
            N -= 1
        else:
            M -= 1
    result = M

    # 2 3 1  의 경우 ( for문을 다 돌았지만 result를 M으로 잡기에 문제가 있을 경우 )
    if N < M * 2:
        result = int(N / 2)
    # 여학생은 무조건 2명 이상
    if N<2:
        result=0
    return result

print(solution(N,M,K))