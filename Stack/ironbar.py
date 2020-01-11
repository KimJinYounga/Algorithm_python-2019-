arrangement = "()(((()())(())()))(())"


def solution(arrangement):
    answer = 0
    line = 0 # 몇차원인지 (예시에서는 3줄 -> 3차원)
    num=0 # 막대 총 갯수

    for i in range(len(arrangement)-1):
        if arrangement[i:i+2]=='()':
            answer += line
        if arrangement[i:i+2]=='))':
            line-=1
            num+=1
        elif arrangement[i:i+2]=='((':
            line+=1

    answer+=num

    return answer


print(solution(arrangement))