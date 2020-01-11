priorities=[1,1,9,1,1,1]
location=0

def solution(priorities, location):
    answer=0
    printer=[]
    list2=[[i]*2 for i in range(len(priorities))] # 2차원 배열 생성 list2=[[value,index], ...]
    for i in range(len(list2)):
        list2[i][0]=priorities[i]
    while len(list2)!=0:
        if list2[0][0] < max(list2)[0]:
            a=list2.pop(0)
            list2.append(a)
        else:
            a=list2.pop(0)
            printer.append(a)

    for i in range(len(printer)):
        if printer[i][1]==location:
            answer=i+1
    return answer

print(solution(priorities, location))