stk = []
num = int(input())
for i in range(num):
    command = input()
    if command.split()[0] == 'push':
        stk.append(command.split()[1])
    elif 'pop' == command:
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())
    elif 'size' == command:
        print(len(stk))
    elif 'empty' == command:
        if len(stk) == 0:
            print(1)
        else:
            print(0)
    elif 'top' == command:
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[len(stk)-1])