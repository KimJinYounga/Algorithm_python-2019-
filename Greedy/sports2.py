n=5
lost=[2,4]
reserve=[1,3,5]

def solution(n, lost, reserve):
    answer = 0
    list=[1 for i in range(0,n)]

    for i in lost:
        list[i-1]-=1

    if len(lost) < len(reserve):
        max=lost
        min=reserve
    else:
        max=reserve
        min=lost

    for i in min:
        for j in max:
            if i==j:
                list[i-1]+=1
                break

    return answer

print(solution(n,lost,reserve))