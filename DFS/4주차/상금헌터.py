import sys
q=lambda: sys.stdin.readline().strip()
T=int(q())
# 상금 1회, 2회 리스트
first=[[500,1],[300,2],[200,3],[50,4],[30,5],[10,6]]
second=[[512,1],[256,2],[128,4],[64,8],[32,16]]

# 입력 리스트
award=[]
lists=[]
lists2=[]
sums=[]
def init():
    for _ in range(T):
        N, M = map(int, q().split())
        award.append([N, M])

def solution():
    for i in award:
        if i[0]!=0:
            sum1 = 0
            for j in range(len(first)):

                sum1 += first[j][1]
                if (sum1 >= i[0]):
                    award1 = first[j][0]
                    lists.append(award1)
                    break
            if sum1 < i[0]:
                lists.append(0)
        else:
            lists.append(0)

        if i[1]!=0:

            sum2 = 0
            for j in range(len(second)):

                sum2 += second[j][1]
                if (sum2 >= i[1]):
                    award1 = second[j][0]
                    lists2.append(award1)
                    break
            if sum2 < i[1]:
                lists2.append(0)
        else:
            lists2.append(0)


    for i in range(T):
        sums.append(int(lists[i])+int(lists2[i]))

    return sums

init()
solution()
for i in sums:
    print(i*10000)