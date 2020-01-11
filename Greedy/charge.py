N=int(input())
A=[500,100,50,10,5,1]

def solution(N,A):
    result=0
    N=1000-N
    for i in range(len(A)):
        result+=int(N/A[i])
        N %= A[i]
    return result

print(solution(N,A))