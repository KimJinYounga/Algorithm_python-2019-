N = int(input())
T = []
TMax = []
count = 0
MaxCount = 0
for i in range(N):
    s,e = map(int, input().split())
    T.append([s,e])
T.sort()
for i in range(0,N):
    count = 0
    TMax = []
    for j in range(i,N):
        size = len(TMax)
        if size==0 :
            TMax.append(T[j])
            count = 1
        else :
            if TMax[-1][1] < T[j][0]:
                TMax.append(T[j])
                count += 1
        if MaxCount < count :
            MaxCount= count
print(MaxCount)