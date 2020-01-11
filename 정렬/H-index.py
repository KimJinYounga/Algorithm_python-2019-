citations=[3, 0, 6, 1, 5]

def solution(citations):
    answer = 0
    citations=sorted(citations, reverse=True)
    for i in range(len(citations)):
        count=i+1
        if citations[i] >= count:
            continue
        else:
            count-=1
            break

    answer=count


    return answer

print(solution(citations))