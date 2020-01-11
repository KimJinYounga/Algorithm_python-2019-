# for i in range('A','Z'):
# print(ord('A'))

import sys

input_s = lambda: sys.stdin.readline()

N=int(input_s())
result = []
distance=0
dis=""
for i in range(N):
    arr=input_s().split()
    for index in range(len(arr[0])):
        distance =  ord(arr[1][index]) - ord(arr[0][index])
        if distance <0:
            distance+=26
        dis = dis + str(distance) + " "
    result.append(dis)
    dis=""


for i in result:
    print("Distances:", i)