n = 5
lost = [2,4]
reserve = [3,4,5]
# 24 [12, 13, 16, 17, 19, 20, 21, 22] [1, 22, 16, 18, 9, 10] 19

def solution(n, lost, reserve):
    sorted(lost)
    sorted(reserve)
    for i in reserve:
        if i in lost:
            lost.remove(i)
            continue
        elif i+1 in lost:
            lost.remove(i+1)
        elif i-1 in lost:
            lost.remove(i-1)
    print(lost)

    return n-len(lost)
print(solution(n,lost,reserve))