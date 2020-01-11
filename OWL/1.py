import sys

input = sys.stdin.readline
N = int(input())
s = ""
result = []

for i in range(N):
    a, b = input().split()
    for j in range(len(a)):
        c = ord(a[j])
        d = ord(b[j])
        r = (d+26)-c if d<c else d-c
        s = s + str(r) + " "
    result.append(s)

for i in result:
    print("Distances:", i)