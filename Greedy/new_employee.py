T = int(input())
result = []


def maximum_new_recruits(T):
   for i in range(T):
       N = int(input())
       score = [list(map(int, input().split())) for j in range(N)]
       score.sort(key=lambda x: x[0]) # 0 인덱스 기준으로 오름차순
       last = score[0][1] # 마지막 원소
       count = 1
       for k in score:
           if last > k[1]:
               last=k[1]
               count+=1
       result.append(count)
   return result


maximum_new_recruits(T)
for i in result:
   print(i)
