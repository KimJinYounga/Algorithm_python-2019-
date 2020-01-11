N = input()                     # 배열
O = input()                         # 순서

list = N.split()
order = O.split()
result = []

list_int = [int(n) for n in list]   # 문자열을 int형으로 전환
list_int.sort()
print(order)
for i in range(len(order)):
    if order[i] == 'A':
        result.append(list_int[0])
    elif order[i] == 'B':
        result.append(list_int[1])
    elif order[i] == 'C':
        result.append(list_int[2])


print(result[0], ' ',result[1], ' ', result[2])