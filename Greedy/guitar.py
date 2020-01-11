N,K = list(map(int, input().split()))
A=[list(map(int, input().split())) for i in range(K)]

def solution(N,A):
    result=0

    count = int(N/6)
    rest = int(N%6)

    if N <6:
        sort_dir(A, 0)
        tmp2=A[0][0]
        sort_dir(A, 1)
        if A[0][1] * N < tmp2:
            result = A[0][1] * N
        else:
            sort_dir(A, 0)
            result = A[0][0]
    else:
        sort_dir(A, 0)
        # 묶음이 더 저렴할 때 => 묶음으로 일단 사고 나머지는 낱개로 사기
        if A[0][0] <= A[0][1] * 6:
            result += A[0][0] * count
            tmp=A[0][0]
            sort_dir(A, 1)
            result += min(A[0][1] * rest, tmp)
            # result += A[0][1] * rest
            #min(A[0][1] * rest, A[0][0])
            # 묶음이 더 비쌀 때=> 낱개로 사기
        else:
            sort_dir(A, 1)
            result += A[0][1] * N

    return result

def sort_dir(A,i):
    A.sort(key=lambda x: x[i])

print(solution(N,A))