result=0
print("입력하세요")
n=int(input())
result+=int(n/500)
n %= 500
result+=int(n/100)
n %= 100
result+=int(n/50)
n %= 50
result+=int(n/10)
print(result)
