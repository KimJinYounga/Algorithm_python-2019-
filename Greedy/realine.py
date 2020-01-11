# import sys
# q = lambda : sys.stdin.readline().strip()
# ans=[]
# case = int(q())
# for i in range(case):
#     ans.append(map(int,q().split(',')))
# print(ans)

import sys

q = lambda: sys.stdin.readline().strip()
case = int(q())

for i in range(case):
	n = int(q())
	s = []
	for _ in range(n):
		s.append(list(map(int, q().split())))
		# s.append([s1,s2])

	print(s)