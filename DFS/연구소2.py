import sys
import copy
input_s = lambda : sys.stdin.readline().strip()

N, M = map(int, input_s().split())
map_info = [list(map(int, input_s().split())) for _ in range(N)]

new_map = []

pillar = [] # 기둥
maximum = -99999


def init():
    # 기둥 놓을 자리 위치 추가
    for i in range(N):
        for j in range(M):
            if map_info[i][j] == 0:
                pillar.append((i, j))   # -> () - 튜플 (같은 자료형 저장할때 쓰임)


# 상, 하 , 좌, 우 검사
def check(x, y):

    # 아래 검사
    if x != N-1 and new_map[x+1][y] == 0:
        down = (x+1, y)
    else: down = False

    # 위 검사
    if x != 0 and new_map[x-1][y] == 0:
        up = (x-1, y)
    else: up = False

    # 왼쪽 검사
    if y != 0 and new_map[x][y-1] == 0:
        left = (x, y-1)
    else: left = False

    # 오른쪽 검사
    if y != M - 1 and new_map[x][y+1] == 0:
        right = (x, y+1)
    else: right = False

    return up, down, left, right

def search_bfs(x, y):
    queue = []
    queue.append((x, y))

    while queue:
        next = queue.pop(0)
        next_x, next_y = next
        result = check(next_x, next_y)
        for case in result:
            if case and case not in queue:
                queue.append(case)

        new_map[next_x][next_y] = 2


def operate_system():
    global maximum
    global new_map
    size = len(pillar)
    for x in range(0, size - 2):
        for y in range(x+1, size - 1):
            for z in range(y+1, size):

                # 기둥 세움
                set_x = pillar[x]
                set_y = pillar[y]
                set_z = pillar[z]

                new_map = copy.deepcopy(map_info)
                new_map[set_x[0]][set_x[1]] = 1
                new_map[set_y[0]][set_y[1]] = 1
                new_map[set_z[0]][set_z[1]] = 1

                # 바이러스 퍼뜨림
                spread_virus(new_map)

                # 안전 지역 개수 셈
                safezone = count_safezone(new_map)

                if safezone > maximum:
                    maximum = safezone
    print(maximum)


def spread_virus(new_map):
    for i in range(N):
        for j in range(M):
            if new_map[i][j] == 2:
                search_bfs(i, j)


def count_safezone(new_map):
    count = 0
    for i in range(N):
        for j in range(M):
            if new_map[i][j] == 0:
                count += 1
    return count

init()
operate_system()