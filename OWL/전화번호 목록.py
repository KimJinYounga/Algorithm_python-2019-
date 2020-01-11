import sys

input_s = lambda: sys.stdin.readline()
N=int(input_s())
for i in range(N):

    M=int(input_s())
    arr = []
    for j in range(M):
        arr.append(input_s().rstrip())

    arr.sort(key=len)
    index = 0
    running=True

    while running:
        tar = arr[index]
        for k in arr[index+1:]:
            if k[:len(tar)] == tar:
                print("NO")
                running=False
            else:
                continue
        index+=1

        if index==M-1:
            if running == True:
                print("YES")
            else:
                tar = arr[index]
