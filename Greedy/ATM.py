N = int(input())
P = list(map(int, input().split()))

def solution(N,P):
    P=sorted(P)
    greedy=[]
    total=0
    for i in range(N):
        total+=P[i]
        greedy.append(total)
    return sum(greedy)

print(solution(N,P))