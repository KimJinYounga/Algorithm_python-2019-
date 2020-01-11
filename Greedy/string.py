A,B=list(input().split())

def solution(A,B):
    result=0
    lenA=len(A)
    lenB = len(B)
    diff=abs(lenA-lenB)

    count = [0 for i in range(diff + 1)]

    for i in range(diff+1):
        for j in range(lenA):
            if A[j]!=B[j+i]:
                count[i]+=1

    result=min(count)
    return result

print(solution(A,B))