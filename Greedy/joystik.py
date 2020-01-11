name="AZAAAZ"

def solution(name):
    answer = 0
    count=0
    if len(name) != 1:
        if name[1] == 'A' or name[-1] == 'A':
            answer += len(name) - 2
        else:
            answer += len(name) - 1

    for i in range(len(name)):
        size = ord(name[i]) - ord('A')
        size2 = ord('Z') - ord(name[i]) + 1
        if size==0 and i !=0 and i != len(name)-1 and name[i]==name[i+1]:
            count+=1
        answer += min(size, size2)
    answer-=count
    return answer

print(solution(name))