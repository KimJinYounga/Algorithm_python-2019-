from operator import itemgetter
numbers = [6, 200, 20]

def solution(numbers):
    answer = ''
    w_count = {}
    list=[[1 for cols in range(3)] for rows in range(len(numbers))]
    numbers.sort(reverse=True)
    for i in range(len(numbers)):
        list[i][0] = numbers[i]
        if numbers[i] < 10:
            list[i][1] = numbers[i]
            list[i][2] = 1

        elif 10 <= numbers[i] < 100:
            list[i][1] = int(numbers[i] / 10)
            list[i][2] = 2

        elif 100 <= numbers[i] < 1000:
            list[i][1] = int(numbers[i] / 100)
            list[i][2] = 3

        else:
            list[i][1] = int(numbers[i] / 1000)
            list[i][2] = 4

        try:
            w_count[list[i][1]] += 1
        except:
            w_count[list[i][1]] = 1
    list.sort(key=itemgetter(1), reverse=True)

    for v in w_count.values():
        if v > 1:
            for i in range(len(list)):
                if list[i][1]==v:
                    if list[i][2]==2:
                        list[i][1] = int(list[i][0] % 10)
                    elif list[i][2]==3:
                        list[i][1] = int(list[i][0] % 100)
                    elif list[i][2]==4:
                        list[i][1] = int(list[i][0] % 1000)

                else:
                    continue
        else:
            continue

    list.sort(key=itemgetter(1), reverse=True)

    for i in range(len(list)):
        list[i][1]=list[i][0]
        answer+=(str(list[i][1]))

    return answer

print(solution(numbers))