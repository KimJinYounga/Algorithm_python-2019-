N=int(input())
time=[list(map(int, input().split())) for i in range(N)]

def solution(N,time):
    temp=0
    result=0
    time.sort(key=lambda x: x[0])
    time.sort(key=lambda x:x[1])
    for i in range(N):
        if temp <= time[i][0]:
            result+=1
            temp=time[i][1]
            print(time[i])
    return result

print(solution(N,time))