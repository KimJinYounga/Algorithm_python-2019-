N=input()

def solution(N):
    list=[]

    for i in N:
        list.append(int(i))
    if 0 in list:
        if sum(list)%3 == 0:
            list.sort(reverse=True)
            list=map(str,list)
            result="".join(list)
            return result

    return -1

print(solution(N))