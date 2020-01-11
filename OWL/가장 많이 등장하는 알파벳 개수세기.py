word="elegance"
def highFrequencyLetterCount():
    # map = {t:2, e:1, s:1}
    map = {}
    for alphabet in word:

        # Key로 Value얻기
        # alphabet이라는 키에 대응되는 Value를 리턴
        if map.get(alphabet)==None:
            map[alphabet]=1
        else:
            map[alphabet]+=1
        print("map ==>", map)
        # print(alphabet)
    max=-1
    for key in map:
        print("key ==> ", key, ", value ==> ", map[key],
              "max ==>", max)
        if map[key] >max:
            max=map[key]
    return max

print("result ==> ", highFrequencyLetterCount())