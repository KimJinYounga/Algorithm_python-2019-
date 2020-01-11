array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, x):
    answer = []
    for i in range(len(x)):
        answer.append(sorted(array[x[i][0]-1:x[i][1]]))
    return answer


print(solution(array, commands))

# 내풀이
# def solution(array, commands):
#     answer = []
#     for i in range(len(commands)):
#         a=commands[i][0]
#         b=commands[i][1]
#         c=commands[i][2]
#         list=array[a-1:b]
#         list.sort()
#         answer.append(list[c-1])
#         answer.append(sorted(array[a-1:b])[c-1])
#
#     return answer

# 내풀이2
# def solution(array, commands):
#     answer = []
#     for i in commands:
#         a,b,c=i
#         answer.append(sorted(array[a-1:b])[c-1])
#     return answer


