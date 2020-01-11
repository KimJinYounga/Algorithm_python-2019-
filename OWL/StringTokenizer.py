# String Tokenzer란?
# 특정 스트링을 내가 원하는 단위로 나누어 주는 로직

string="13+3*{24*(35-46.76)-89}"

def stringTokenizer(string, deli):
    result=[]
    accu=""
    for chr in string:
        if chr in deli:
            if accu !="":
                result.append(accu)
                accu=""
            result.append(chr)
        else:
            accu=accu+chr
        # print(chr)
    return result

result=stringTokenizer(string, "+-*/(){}^")
print(result)