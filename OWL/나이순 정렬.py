import sys

input_s = lambda: sys.stdin.readline()

M = int(input_s())
abj = [list(input_s().split()) for i in range(M)]

# sort할 때는 대상이 String 형이면 안됌. int형이어야함
# String 형이면 ==>  '10' < '9' 와 같은 오류가 생길 수 있음
for i in abj:
    i[0]=int(i[0])
abj.sort(key=lambda x: x[0])

for i in range(M):
    print(abj[i][0],abj[i][1])