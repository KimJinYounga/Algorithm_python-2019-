# import math
#
# 채연=(0,0)
# 나연=(2,2)
#
# def get두점사이거리(점1,점2):
#     x축거리=나연[0]-채연[0]
#     y축거리=나연[1]-채연[1]
#     x축거리plusy축거리=math.pow(x축거리, 2)+\
#     math.pow(y축거리,2)
#     return math.sqrt(x축거리plusy축거리)
#
# result=get두점사이거리(채연, 나연)
# print("채연이와 나영이의 거리는:", result)
# print("a와 b의 거리는:", get두점사이거리((1,2),(3,4)))

import math


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point2D(x=30, y=20)  # 점1
p2 = Point2D(x=60, y=50)  # 점2

a = p2.x - p1.x  # 선 a의 길이
b = p2.y - p1.y  # 선 b의 길이

c = math.sqrt((a * a) + (b * b))  # (a * a) + (b * b)의 제곱근을 구함
print(c)
